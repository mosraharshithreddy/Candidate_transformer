from pprint import pprint

from src.parsers.pdf_parser import PDFParser
from src.extractor import extract_candidate
from src.canonical_mapper import CanonicalMapper

parser = PDFParser()

text = parser.parse("input/resume.pdf")

candidate_dict = extract_candidate(text)

mapper = CanonicalMapper()

candidate = mapper.map(
    candidate_dict,
    source="resume"
)

print("=" * 80)
print("CANONICAL CANDIDATE")
print("=" * 80)

pprint(candidate.model_dump())

print("=" * 80)