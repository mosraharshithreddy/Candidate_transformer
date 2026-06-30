import json
import os

from src.parsers.pdf_parser import PDFParser
from src.parsers.csv_parser import CSVParser
from src.extractor import extract_candidate
from src.canonical_mapper import CanonicalMapper
from src.merger.merge import CandidateMerger
from src.confidence.scorer import ConfidenceScorer
from src.validator.validator import CandidateValidator
from src.validator.identity_validator import IdentityValidator
from src.projector.projector import CandidateProjector
from src.github.github_client import GitHubClient


def process_candidate(
    resume_path,
    recruiter_csv_path,
    github_username=None,
):

    mapper = CanonicalMapper()

    # =====================================================
    # Resume
    # =====================================================

    pdf_parser = PDFParser()

    resume_text = pdf_parser.parse(
        resume_path
    )

    extracted_resume = extract_candidate(
        resume_text
    )

    resume_candidate = mapper.map(
        extracted_resume,
        source="resume",
    )

    # =====================================================
    # Recruiter CSV
    # =====================================================

    csv_parser = CSVParser()

    recruiter_rows = csv_parser.parse(
        recruiter_csv_path
    )

    if not recruiter_rows:
        raise Exception(
            "Recruiter CSV is empty."
        )

    recruiter_candidate = mapper.map(
        recruiter_rows[0],
        source="recruiter_csv",
    )

    # =====================================================
    # Identity Validation
    # =====================================================

    identity_validator = IdentityValidator()

    identity_errors = identity_validator.validate(
        resume_candidate,
        recruiter_candidate,
    )

    if identity_errors:

        raise Exception(
            "\n\n".join(identity_errors)
        )

    # =====================================================
    # GitHub
    # =====================================================

    github_candidate = None

    if not github_username:

        github_username = recruiter_rows[0].get(
            "github",
            ""
        ).strip()

    if github_username:

        try:

            github_client = GitHubClient()

            github_data = github_client.fetch(
                github_username
            )

            github_candidate = mapper.map(
                github_data,
                source="github",
            )

        except Exception:

            github_candidate = None

    # =====================================================
    # Merge
    # =====================================================

    merger = CandidateMerger()

    if github_candidate:

        merged_candidate = merger.merge(
            resume_candidate,
            recruiter_candidate,
            github_candidate,
        )

    else:

        merged_candidate = merger.merge(
            resume_candidate,
            recruiter_candidate,
        )

    # =====================================================
    # Confidence
    # =====================================================

    scorer = ConfidenceScorer()

    scorer.score(
        merged_candidate
    )

    # =====================================================
    # Final Validation
    # =====================================================

    validator = CandidateValidator()

    errors = validator.validate(
        merged_candidate
    )

    if errors:

        raise Exception(
            "\n".join(errors)
        )

    # =====================================================
    # Output Folder
    # =====================================================

    os.makedirs(
        "output",
        exist_ok=True,
    )

    # =====================================================
    # Canonical JSON
    # =====================================================

    with open(
        "output/candidate.json",
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            merged_candidate.model_dump(),
            f,
            indent=4,
            ensure_ascii=False,
        )

    # =====================================================
    # Projected JSON
    # =====================================================

    projector = CandidateProjector(
        "config/default.json"
    )

    projector.save(
        merged_candidate,
        "output/projected_candidate.json",
    )

    return merged_candidate