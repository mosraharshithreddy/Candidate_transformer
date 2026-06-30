import uuid

from src.models import (
    Candidate,
    Location,
    Links,
    Skill,
    Experience,
    Education,
    Provenance,
)


class CanonicalMapper:
    """
    Converts extracted data from any source
    into the canonical Candidate model.
    """

    def map(self, data: dict, source: str = "resume") -> Candidate:

        # =====================================================
        # Candidate ID
        # =====================================================
        candidate_id = data.get("candidate_id")

        if not candidate_id:
            candidate_id = str(uuid.uuid4())

        # =====================================================
        # Location
        # =====================================================
        location = Location()

        location_data = data.get("location")

        if isinstance(location_data, dict):

            location.city = location_data.get("city")
            location.region = location_data.get("region")
            location.country = location_data.get("country")

        elif isinstance(location_data, str):

            parts = [p.strip() for p in location_data.split(",")]

            if len(parts) >= 1:
                location.city = parts[0]

            if len(parts) >= 2:
                location.region = parts[1]

            if len(parts) >= 3:
                location.country = parts[2]

        # =====================================================
        # Links
        # =====================================================
        links_data = data.get("links", {})

        if not isinstance(links_data, dict):
            links_data = {}

        links = Links(
            linkedin=links_data.get("linkedin"),
            github=links_data.get("github"),
            portfolio=links_data.get("portfolio"),
            other=links_data.get("other"),
        )

        # =====================================================
        # Skills
        # =====================================================
        raw_skills = data.get("skills", [])

        if isinstance(raw_skills, str):
            raw_skills = [
                s.strip()
                for s in raw_skills.split(",")
                if s.strip()
            ]

        skills = []

        for skill in raw_skills:
            skills.append(
                Skill(
                    name=skill,
                    confidence=1.0,
                    sources=[source],
                )
            )

        # =====================================================
        # Education
        # =====================================================
        education = []

        for edu in data.get("education", []):

            graduation_year = edu.get("graduation_year")

            try:
                graduation_year = (
                    int(graduation_year)
                    if graduation_year
                    else None
                )
            except Exception:
                graduation_year = None

            education.append(
                Education(
                    institution=edu.get("institution"),
                    degree=edu.get("degree"),
                    field=edu.get("field"),
                    graduation_year=graduation_year,
                )
            )

        # =====================================================
        # Experience
        # =====================================================
        experience = []

        for exp in data.get("experience", []):

            experience.append(
                Experience(
                    company=exp.get("company"),
                    title=exp.get("title"),
                    start_date=exp.get("start_date"),
                    end_date=exp.get("end_date"),
                    summary=exp.get("summary"),
                )
            )

        # =====================================================
        # Years of Experience
        # =====================================================
        years_experience = data.get("years_experience")

        try:
            years_experience = (
                float(years_experience)
                if years_experience not in ("", None)
                else None
            )
        except Exception:
            years_experience = None

        # =====================================================
        # Provenance
        # =====================================================
        provenance = []

        for field in data.keys():

            provenance.append(
                Provenance(
                    field=field,
                    source=source,
                    extraction_method="regex",
                )
            )

        # =====================================================
        # Candidate
        # =====================================================
        candidate = Candidate(

            candidate_id=candidate_id,

            full_name=data.get("full_name"),

            emails=[
                data["email"]
            ] if data.get("email") else [],

            phones=[
                data["phone"]
            ] if data.get("phone") else [],

            location=location,

            links=links,

            headline=data.get("headline"),

            years_experience=years_experience,

            skills=skills,

            experience=experience,

            education=education,

            provenance=provenance,

            overall_confidence=0.0,
        )

        return candidate