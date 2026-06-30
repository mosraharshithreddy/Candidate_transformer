from src.parsers.pdf_parser import PDFParser
from src.extractor import extract_candidate
from src.canonical_mapper import CanonicalMapper
from src.merger.merge import CandidateMerger
from src.confidence.scorer import ConfidenceScorer
from src.validator.validator import CandidateValidator

parser = PDFParser()
text = parser.parse("input/resume.pdf")

mapper = CanonicalMapper()

resume = mapper.map(
    extract_candidate(text),
    source="resume"
)

recruiter = mapper.map(
    {
        "full_name": "Mosra Harshith Reddy",
        "email": "harshithreddymosra@gmail.com",
        "phone": "+919704745443",
        "headline": "Software Engineer",
        "years_experience": 2,
        "links": {},
        "location": {},
        "skills": ["Python", "SQL", "Docker"],
        "education": [],
        "experience": []
    },
    source="recruiter_csv"
)

merged = CandidateMerger().merge(resume, recruiter)

ConfidenceScorer().score(merged)

validator = CandidateValidator()

errors = validator.validate(merged)

print("=" * 70)

if errors:
    print("Validation Failed")
    for error in errors:
        print("-", error)
else:
    print("Validation Successful ✅")

print("=" * 70)