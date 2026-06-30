from src.pipeline import process_candidate


def main():

    candidate = process_candidate(
        "input/resume.pdf",
        "input/recruiter.csv",
    )

    print()
    print("=" * 60)
    print("Pipeline Completed Successfully")
    print("=" * 60)

    print(candidate.full_name)


if __name__ == "__main__":
    main()