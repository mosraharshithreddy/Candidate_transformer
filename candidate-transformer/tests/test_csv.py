from src.parsers.csv_parser import CSVParser

parser = CSVParser()

records = parser.parse("input/recruiter.csv")

print(records)