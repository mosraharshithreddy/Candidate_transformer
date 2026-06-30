import pandas as pd
from pathlib import Path


class CSVParser:
    """
    Reads recruiter CSV files and returns
    a list of candidate dictionaries.
    """

    REQUIRED_COLUMNS = [
        "candidate_id",
        "full_name",
        "email",
        "phone",
        "headline",
        "years_experience",
        "skills",
        "location",
    ]

    def parse(self, file_path: str) -> list[dict]:
        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(f"CSV file not found: {file_path}")

        try:
            df = pd.read_csv(file, dtype=str)

        except Exception as e:
            raise ValueError(f"Unable to read CSV: {e}")

        missing = [
            col for col in self.REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {missing}"
            )

        records = (
        df.fillna("")
            .apply(lambda col: col.str.strip() if col.dtype == "object" else col)
            .to_dict(orient="records")
        )

        return records