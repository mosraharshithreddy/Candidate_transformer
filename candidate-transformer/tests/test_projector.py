from src.parsers.pdf_parser import PDFParser
from src.extractor import extract_candidate
from src.canonical_mapper import CanonicalMapper
from src.merger.merge import CandidateMerger
from src.confidence.scorer import ConfidenceScorer
from src.validator.validator import CandidateValidator
from src.projector.projector import CandidateProjector

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

candidate = CandidateMerger().merge(
    resume,
    recruiter
)

ConfidenceScorer().score(candidate)

errors = CandidateValidator().validate(candidate)

if errors:

    print(errors)

else:

    CandidateProjector().save(
        candidate,
        "output/projected_candidate.json",
    )