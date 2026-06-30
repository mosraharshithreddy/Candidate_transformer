from pprint import pprint

from src.parsers.pdf_parser import PDFParser
from src.extractor import extract_candidate
from src.canonical_mapper import CanonicalMapper
from src.merger.merge import CandidateMerger
from src.confidence.scorer import ConfidenceScorer

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

print("=" * 80)
print("OVERALL CONFIDENCE:", merged.overall_confidence)
print("=" * 80)

pprint(merged.model_dump())