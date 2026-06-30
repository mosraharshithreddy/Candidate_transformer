from pprint import pprint

from src.parsers.pdf_parser import PDFParser
from src.extractor import extract_candidate

parser = PDFParser()

text = parser.parse("input/resume.pdf")

candidate = extract_candidate(text)

pprint(candidate)