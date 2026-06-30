import json
import os

from src.models import Candidate
from src.normalizers.phone import normalize_phone
from src.normalizers.skill import normalize_skill


class CandidateProjector:

    def __init__(self, config_path="config/default.json"):

        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def _extract(self, data, path):

        if path.endswith("[]"):
            return data.get(path[:-2], [])

        if path == "emails[0]":
            emails = data.get("emails", [])
            return emails[0] if emails else None

        if path == "phones[0]":
            phones = data.get("phones", [])
            return phones[0] if phones else None

        if path == "skills[].name":
            return [
                skill["name"]
                for skill in data.get("skills", [])
            ]

        return data.get(path)

    def _normalize(self, value, normalize_type):

        if value is None:
            return value

        if normalize_type == "E164":
            return normalize_phone(value)

        if normalize_type == "canonical":

            if isinstance(value, list):
                return [
                    normalize_skill(v)
                    for v in value
                ]

            return normalize_skill(value)

        return value

    def _validate(self, name, value, expected_type, required):

        if required and value is None:
            raise ValueError(
                f"Required field '{name}' is missing."
            )

        if value is None:
            return

        if expected_type == "string":

            if not isinstance(value, str):
                raise TypeError(
                    f"{name} must be a string."
                )

        elif expected_type == "string[]":

            if not isinstance(value, list):
                raise TypeError(
                    f"{name} must be a list."
                )

            for item in value:

                if not isinstance(item, str):
                    raise TypeError(
                        f"{name} must contain only strings."
                    )

    def project(self, candidate: Candidate):

        candidate_dict = candidate.model_dump()

        output = {}

        for field in self.config["fields"]:

            output_name = field["path"]

            source = field.get(
                "from",
                output_name,
            )

            value = self._extract(
                candidate_dict,
                source,
            )

            # -------------------------
            # Missing value policy
            # -------------------------
            if value is None:

                policy = self.config.get(
                    "on_missing",
                    "null",
                )

                if policy == "omit":
                    continue

                if policy == "error":
                    raise ValueError(
                        f"Missing required value: {source}"
                    )

            # -------------------------
            # Normalization
            # -------------------------
            normalize = field.get("normalize")

            if normalize:
                value = self._normalize(
                    value,
                    normalize,
                )

            # -------------------------
            # Validation
            # -------------------------
            self._validate(
                output_name,
                value,
                field.get("type"),
                field.get("required", False),
            )

            output[output_name] = value

        # -------------------------
        # Confidence
        # -------------------------
        if self.config.get(
            "include_confidence",
            False,
        ):

            output[
                "overall_confidence"
            ] = candidate.overall_confidence

        # -------------------------
        # Provenance
        # -------------------------
        if self.config.get(
            "include_provenance",
            False,
        ):

            output[
                "provenance"
            ] = candidate_dict["provenance"]

        return output

    def save(
        self,
        candidate: Candidate,
        output_path: str,
    ):

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True,
        )

        projected = self.project(candidate)

        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                projected,
                f,
                indent=4,
                ensure_ascii=False,
            )

        print(
            f"\nProjected JSON saved to:\n{output_path}"
        )