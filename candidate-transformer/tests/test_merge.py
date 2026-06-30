from pprint import pprint

from src.parsers.pdf_parser import PDFParser
from src.extractor import extract_candidate
from src.canonical_mapper import CanonicalMapper
from src.merger.merge import CandidateMerger

# -----------------------------
# Resume Candidate
# -----------------------------
parser = PDFParser()

text = parser.parse("input/resume.pdf")

mapper = CanonicalMapper()

resume_candidate = mapper.map(
    extract_candidate(text),
    source="resume"
)

# -----------------------------
# Simulated Recruiter Candidate
# -----------------------------
recruiter_data = {
    "full_name": "Mosra Harshith Reddy",
    "email": "harshithreddymosra@gmail.com",
    "phone": "+919704745443",

    "headline": "Software Engineer",

    "years_experience": 2,

    "links": {
        "linkedin": "https://linkedin.com/in/harshith",
        "github": "https://github.com/harshith"
    },

    "location": {
        "city": "Hyderabad",
        "region": "Telangana",
        "country": "India"
    },

    "skills": [
        "Python",
        "SQL",
        "Docker",
        "GitHub"
    ],

    "education": [],

    "experience": []
}

recruiter_candidate = mapper.map(
    recruiter_data,
    source="recruiter_csv"
)

# -----------------------------
# Merge
# -----------------------------
merger = CandidateMerger()

merged_candidate = merger.merge(
    resume_candidate,
    recruiter_candidate
)

# -----------------------------
# Print
# -----------------------------
print("=" * 80)
print("MERGED CANDIDATE")
print("=" * 80)

pprint(merged_candidate.model_dump())

print("=" * 80)