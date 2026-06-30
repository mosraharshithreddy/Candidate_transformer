# Candidate Profile Transformer

## Overview

Candidate Profile Transformer is a Python-based application that consolidates candidate information from multiple heterogeneous sources into a unified canonical profile.

The application extracts candidate information from:

- Resume (PDF)
- Recruiter CSV
- GitHub Profile (Optional)

The extracted information is normalized, validated, merged, and transformed into a standardized candidate profile. The system also generates configurable JSON outputs using a runtime projection configuration.

A Flask-based web interface allows users to upload files, visualize the generated candidate profile, and download the resulting JSON files.

---

## Features

- Resume PDF Parsing
- Recruiter CSV Parsing
- GitHub Profile Enrichment
- Candidate Matching
- Identity Validation
- Canonical Candidate Schema
- Multi-Source Profile Merging
- Skill Aggregation
- Confidence Score Calculation
- Provenance Tracking
- Runtime JSON Projection
- Canonical JSON Generation
- Projected JSON Generation
- Flask Web Dashboard
- Downloadable JSON Outputs

---

## System Architecture

```text
                  Resume PDF
                       │
                       ▼
                 PDF Parser
                       │
                       ▼
            Candidate Extractor
                       │
                       ▼
             Canonical Mapper
                       ▲
                       │
          Recruiter CSV Parser
                       │
                       ▼
            Candidate Matcher
      (Email → Phone → Full Name)
                       │
                       ▼
           Identity Validation
                       │
                       ▼
           GitHub Enrichment
                       │
                       ▼
              Merge Engine
                       │
                       ▼
         Confidence Scoring
                       │
                       ▼
           Schema Validation
                       │
                       ▼
      Runtime JSON Projection
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
    candidate.json        projected_candidate.json
```

---

## Technology Stack

### Backend

- Python 3.10+
- Flask
- Pydantic

### Parsing

- pdfplumber
- CSV
- Regular Expressions

### Frontend

- HTML5
- Bootstrap 5

---

## Project Structure

```text
candidate-profile-transformer/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│   └── default.json
│
├── input/
│   ├── resume.pdf
│   └── recruiter.csv
│
├── output/
│   ├── candidate.json
│   └── projected_candidate.json
│
├── uploads/
│
├── src/
│   ├── confidence/
│   ├── github/
│   ├── merger/
│   ├── parsers/
│   ├── projector/
│   ├── utils/
│   ├── validator/
│   ├── canonical_mapper.py
│   ├── extractor.py
│   ├── models.py
│   └── pipeline.py
│
├── templates/
│
└── tests/
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/candidate-profile-transformer.git
```

Move into the project directory.

```bash
cd candidate-profile-transformer
```

(Optional) Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Project

The application can be executed in two ways.

### Option 1 – Command Line Pipeline

Place the input files inside the **input** directory.

```text
input/
├── resume.pdf
└── recruiter.csv
```

Run the pipeline.

```bash
python main.py
```

The pipeline performs the following steps:

- Parse Resume PDF
- Parse Recruiter CSV
- Match Candidate
- Validate Candidate Identity
- Retrieve GitHub Profile (Optional)
- Merge Candidate Information
- Calculate Confidence Score
- Validate Candidate Schema
- Generate Canonical JSON
- Generate Projected JSON

The generated files are stored inside:

```text
output/
├── candidate.json
└── projected_candidate.json
```

---

### Option 2 – Flask Web Application

Run the Flask application.

```bash
python app.py
```

Open your browser.

```text
http://127.0.0.1:5000
```

### Application Workflow

1. Upload Resume PDF.
2. Upload Recruiter CSV.
3. Enter GitHub Username (Optional).
4. Click **Generate Candidate Profile**.
5. The application:
   - Parses the uploaded resume.
   - Reads the recruiter CSV.
   - Finds the matching candidate.
   - Validates candidate identity.
   - Retrieves GitHub information (if provided).
   - Merges all available information.
   - Calculates the confidence score.
   - Generates Canonical and Projected JSON files.
6. View the generated candidate profile.
7. Download the generated JSON outputs.

---

## Candidate Matching

The recruiter CSV may contain one or multiple candidate records.

The application automatically locates the correct candidate using the following priority:

1. Email Address
2. Phone Number
3. Full Name

Only the matched recruiter record is merged with the uploaded resume.

---

## Identity Validation

Before merging, the application validates that the uploaded Resume and Recruiter CSV belong to the same candidate.

Validation is performed using:

- Full Name
- Email Address
- Phone Number

If validation fails, the merge process is stopped and a detailed validation report is displayed.

---

## Output Files

### Canonical Candidate Profile

```text
output/candidate.json
```

Contains the standardized candidate profile generated after merging all available sources.

### Projected Candidate Profile

```text
output/projected_candidate.json
```

Generated using the runtime configuration file:

```text
config/default.json
```

The projection layer supports:

- Field Selection
- Field Renaming
- Nested Field Mapping
- Confidence Toggle
- Provenance Toggle

without modifying the application source code.

---

## Future Enhancements

- LinkedIn Integration
- OCR Support for Scanned Resumes
- AI-assisted Resume Parsing
- REST API Development
- Database Integration
- Batch Candidate Processing
- Docker Deployment
- Authentication & User Management

---

## Author

**Mosra Harshith Reddy**

B.Tech – Computer Science (Cyber Security)

Institute of Aeronautical Engineering

---

## License

This project was developed for educational purposes and as part of the **Eightfold.ai Hiring Assignment**.