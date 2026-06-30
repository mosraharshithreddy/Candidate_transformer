import re
from typing import List

from src.normalizers.phone import normalize_phone
from src.normalizers.skill import normalize_skill


MONTHS = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def normalize_month_year(date_str):
    if not date_str:
        return None

    parts = date_str.split()

    if len(parts) != 2:
        return date_str

    month, year = parts

    month = MONTHS.get(month)

    if month:
        return f"{year}-{month}"

    return date_str


def extract_name(text: str) -> str:

    for line in text.splitlines():
        line = line.strip()

        if line:
            return line

    return ""


def extract_email(text: str) -> str:

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


def extract_phone(text: str) -> str:

    pattern = r"\+?\d[\d\s()-]{8,}\d"

    match = re.search(pattern, text)

    if not match:
        return ""

    return normalize_phone(match.group()) or ""


def extract_links(text: str):

    links = {
        "linkedin": None,
        "github": None,
        "portfolio": None,
    }

    patterns = {
        "linkedin": r"https?://(?:www\.)?linkedin\.com/[^\s]+",
        "github": r"https?://(?:www\.)?github\.com/[^\s]+",
        "portfolio": r"https?://[^\s]+",
    }

    for key, pattern in patterns.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            links[key] = match.group()

    return links


def extract_skills(text: str):

    match = re.search(
        r"TECHNICAL SKILLS(.*?)INTERNSHIP",
        text,
        re.DOTALL | re.IGNORECASE,
    )

    if not match:
        return []

    section = match.group(1)

    categories = [
        "Languages",
        "Web and Backend",
        "AI/ML",
        "Security Tools",
        "Version Control",
    ]

    skills = []

    for line in section.splitlines():

        line = line.strip()

        if not line:
            continue

        for cat in categories:

            if line.startswith(cat):
                line = line.replace(cat, "").strip()

        for skill in line.split(","):

            skill = normalize_skill(skill.strip())

            if skill:
                skills.append(skill)

    return list(dict.fromkeys(skills))


def extract_education(text: str):

    match = re.search(
        r"EDUCATION(.*?)TECHNICAL SKILLS",
        text,
        re.DOTALL | re.IGNORECASE,
    )

    if not match:
        return []

    lines = [
        l.strip()
        for l in match.group(1).splitlines()
        if l.strip()
    ]

    education = []

    i = 0

    while i < len(lines):

        institution = lines[i]

        degree = ""

        if i + 1 < len(lines):
            degree = lines[i + 1]

        years = re.findall(r"(19\d{2}|20\d{2})", institution + " " + degree)

        graduation_year = years[-1] if years else None

        institution = re.sub(
            r"Expected Graduation-?\d{4}",
            "",
            institution,
            flags=re.IGNORECASE,
        )

        institution = re.sub(
            r"\b(19|20)\d{2}\b(\s*-\s*\d{4})?",
            "",
            institution,
        )

        institution = institution.strip()

        education.append(
            {
                "institution": institution,
                "degree": degree,
                "graduation_year": graduation_year,
            }
        )

        i += 2

    return education


def extract_experience(text: str):

    match = re.search(
        r"INTERNSHIP(.*?)PROJECTS",
        text,
        re.DOTALL | re.IGNORECASE,
    )

    if not match:
        return []

    lines = [
        l.strip()
        for l in match.group(1).splitlines()
        if l.strip()
    ]

    if len(lines) < 3:
        return []

    company = lines[0]

    title = lines[1]

    start = None

    end = None

    date_match = re.search(
        r"([A-Za-z]+ \d{4})\s*-\s*([A-Za-z]+ \d{4})",
        company,
    )

    if date_match:

        start = normalize_month_year(date_match.group(1))

        end = normalize_month_year(date_match.group(2))

        company = company.replace(
            date_match.group(),
            ""
        ).strip()

    summary = " ".join(lines[2:])

    return [
        {
            "company": company,
            "title": title,
            "start_date": start,
            "end_date": end,
            "summary": summary,
        }
    ]


def extract_candidate(text: str):

    return {
        "full_name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "links": extract_links(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
    }