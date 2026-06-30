# Candidate Profile Transformer

A Python-based application that transforms candidate information from multiple heterogeneous sources into a unified canonical profile. The system parses Resume PDFs, Recruiter CSV files, and GitHub profiles, merges the extracted information into a standardized schema, validates identity consistency, calculates confidence scores, tracks data provenance, and generates configurable JSON outputs.

The project also includes a Flask-based web application for uploading candidate documents, visualizing the unified profile, and downloading the generated JSON files.

---

# Features

- Resume PDF Parsing
- Recruiter CSV Parsing
- GitHub Profile Enrichment
- Canonical Candidate Schema
- Candidate Identity Matching
- Multi-source Profile Merging
- Skill Aggregation
- Confidence Score Calculation
- Provenance Tracking
- Candidate Validation
- Configurable JSON Projection
- Canonical JSON Generation
- Projected JSON Generation
- Flask Web Interface
- Downloadable JSON Outputs

---

# Project Architecture

```
                Resume PDF
                     │
                     ▼
              PDF Text Parser
                     │
                     ▼
          Candidate Information Extractor
                     │
                     ▼
             Canonical Candidate Mapper
                     │
                     │
Recruiter CSV ───────┘
                     │
                     ▼
          Candidate Matcher
      (Email → Phone → Name)
                     │
                     ▼
          Identity Validation
                     │
                     ▼
            GitHub Enrichment
                     │
                     ▼
             Candidate Merger
                     │
                     ▼
          Confidence Scoring
                     │
                     ▼
             Schema Validation
                     │
                     ▼
      Canonical Candidate Profile
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
Candidate JSON          Projected JSON
```

---

# Technology Stack

### Backend

- Python 3.10+
- Flask
- Pydantic

### Parsing

- pdfplumber
- Regular Expressions

### Frontend

- HTML5
- Bootstrap 5
- Bootstrap Icons

### Data Format

- JSON
- CSV
- PDF

---

# Project Structure

```
candidate-transformer/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│     └── default.json
│
├── input/
│     ├── resume.pdf
│     └── recruiter.csv
│
├── output/
│     ├── candidate.json
│     └── projected_candidate.json
│
├── uploads/
│
├── src/
│
│     ├── confidence/
│     │      └── scorer.py
│
│     ├── github/
│     │      └── github_client.py
│
│     ├── merger/
│     │      └── merge.py
│
│     ├── normalizers/
│
│     ├── parsers/
│     │      ├── pdf_parser.py
│     │      └── csv_parser.py
│
│     ├── projector/
│     │      └── projector.py
│
│     ├── validator/
│     │      ├── validator.py
│     │      └── identity_validator.py
│
│     ├── utils/
│     │      └── candidate_matcher.py
│
│     ├── canonical_mapper.py
│     ├── extractor.py
│     ├── models.py
│     └── pipeline.py
│
├── templates/
│     ├── index.html
│     ├── result.html
│     └── error.html
│
└── tests/
```

---

# Workflow

The application follows the pipeline below:

### Step 1

Upload

- Resume PDF
- Recruiter CSV
- GitHub Username (Optional)

↓

### Step 2

Parse Resume PDF

↓

### Step 3

Read Recruiter CSV

↓

### Step 4

Automatically find the matching recruiter record using

- Email
- Phone Number
- Full Name

↓

### Step 5

Validate candidate identity

↓

### Step 6

Fetch GitHub Profile

↓

### Step 7

Merge candidate information

↓

### Step 8

Calculate confidence score

↓

### Step 9

Validate schema

↓

### Step 10

Generate

- Canonical JSON
- Projected JSON

---

# Canonical Candidate Schema

The canonical profile contains:

- Candidate ID
- Full Name
- Email
- Phone
- Location
- Headline
- Years of Experience
- Skills
- Experience
- Education
- Links
- Provenance
- Overall Confidence

---

# Candidate Matching

The application supports recruiter CSV files containing multiple candidates.

The matching priority is:

1. Email Address
2. Phone Number
3. Full Name

Only after locating the correct recruiter record does the application proceed with merging.

If no matching candidate is found, the application reports a validation error.

---

# Identity Validation

To prevent incorrect merges, the application validates:

- Full Name
- Email Address
- Phone Number

If the Resume and Recruiter CSV belong to different candidates, the merge process is stopped and an error page is displayed.

---

# Confidence Scoring

The system calculates an overall confidence score based on the completeness and consistency of information collected from multiple sources.

The confidence score ranges between:

```
0.0 – 1.0
```

where

```
1.0
```

indicates a highly reliable candidate profile.

---

# Provenance Tracking

Every extracted field records its origin.

Example:

```json
{
    "field": "skills",
    "source": "resume",
    "extraction_method": "regex"
}
```

This provides complete traceability for all candidate information.

---

# Configurable Projection

Instead of modifying application code, the output format is controlled using

```
config/default.json
```

The configuration supports:

- Field Selection
- Field Renaming
- Nested Mapping
- Include/Exclude Provenance
- Include/Exclude Confidence
- Missing Value Handling

Example

```json
{
    "path": "primary_email",
    "from": "emails[0]"
}
```

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Command Line Version

```bash
python main.py
```

---

## Run Flask Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# Input Files

Resume

```
PDF
```

Recruiter Data

```
CSV
```

GitHub

```
Username (Optional)
```

---

# Output Files

```
output/

candidate.json

projected_candidate.json
```

---

# Web Application

The Flask interface allows users to

- Upload Resume PDF
- Upload Recruiter CSV
- Provide GitHub Username
- Generate Unified Candidate Profile
- Visualize Candidate Information
- Download Canonical JSON
- Download Projected JSON

---

# Sample Dashboard

The dashboard displays

- Personal Information
- Skills
- Experience
- Education
- Pipeline Status
- Confidence Score
- Download Buttons

---

# Testing

The project contains unit tests for

- PDF Parser
- CSV Parser
- Skill Extraction
- Canonical Mapping
- Merge Engine
- Validation
- Confidence Scoring
- GitHub Integration
- Projection
- Candidate Matching

Run tests using

```bash
python -m tests.test_pdf
```

Example

```bash
python -m tests.test_github
```

---

# Future Enhancements

- LinkedIn Profile Integration
- OCR Support for Scanned Resumes
- AI-based Resume Parsing
- Database Integration
- REST API
- Docker Deployment
- Kubernetes Deployment
- Authentication
- Recruiter Dashboard
- Batch Candidate Processing

---

# Screenshots

Add screenshots here after uploading them.

Example

```
Home Page

Result Dashboard

Validation Error

Generated JSON
```

---

# Author

**Mosra Harshith Reddy**

B.Tech Computer Science (Cyber Security)

Institute of Aeronautical Engineering

---

# License

This project is developed for educational and assessment purposes.