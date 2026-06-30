from src.parsers.pdf_parser import PDFParser

parser = PDFParser()

text = parser.parse("input/resume.pdf")

print(text)