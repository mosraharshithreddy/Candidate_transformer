from copy import deepcopy
from src.models import Candidate


class CandidateMerger:
    """
    Merge multiple Candidate objects into a single canonical profile.

    Source Priority:
        recruiter_csv > resume
    """

    def merge(self, *candidates: Candidate) -> Candidate:

        if not candidates:
            raise ValueError("No candidates provided.")

        merged = deepcopy(candidates[0])

        for candidate in candidates[1:]:

            # ------------------------------------------------
            # Candidate ID
            # ------------------------------------------------
            # Prefer recruiter/system IDs over generated UUIDs
            if (
                candidate.candidate_id
                and not candidate.candidate_id.startswith(("000", "tmp"))
            ):
                merged.candidate_id = candidate.candidate_id

            # ------------------------------------------------
            # Full Name
            # ------------------------------------------------
            if candidate.full_name:
                merged.full_name = candidate.full_name

            # ------------------------------------------------
            # Emails
            # ------------------------------------------------
            merged.emails = list(
                dict.fromkeys(
                    merged.emails + candidate.emails
                )
            )

            # ------------------------------------------------
            # Phones
            # ------------------------------------------------
            merged.phones = list(
                dict.fromkeys(
                    merged.phones + candidate.phones
                )
            )

            # ------------------------------------------------
            # Headline
            # ------------------------------------------------
            if candidate.headline:
                merged.headline = candidate.headline

            # ------------------------------------------------
            # Years Experience
            # ------------------------------------------------
            if candidate.years_experience is not None:
                merged.years_experience = candidate.years_experience

            # ------------------------------------------------
            # Location
            # ------------------------------------------------
            if candidate.location.city:
                merged.location.city = candidate.location.city

            if candidate.location.region:
                merged.location.region = candidate.location.region

            if candidate.location.country:
                merged.location.country = candidate.location.country

            # ------------------------------------------------
            # Links
            # ------------------------------------------------
            if candidate.links.linkedin:
                merged.links.linkedin = candidate.links.linkedin

            if candidate.links.github:
                merged.links.github = candidate.links.github

            if candidate.links.portfolio:
                merged.links.portfolio = candidate.links.portfolio

            if candidate.links.other:
                merged.links.other = candidate.links.other

            # ------------------------------------------------
            # Skills
            # ------------------------------------------------
            skill_map = {
                skill.name.lower(): skill
                for skill in merged.skills
            }

            for skill in candidate.skills:

                key = skill.name.lower()

                if key in skill_map:

                    existing = skill_map[key]

                    existing.sources = list(
                        dict.fromkeys(
                            existing.sources + skill.sources
                        )
                    )

                    existing.confidence = max(
                        existing.confidence,
                        skill.confidence,
                    )

                else:

                    skill_map[key] = skill

            merged.skills = list(skill_map.values())

            # ------------------------------------------------
            # Education
            # ------------------------------------------------
            for edu in candidate.education:

                exists = any(
                    e.institution == edu.institution
                    and e.degree == edu.degree
                    for e in merged.education
                )

                if not exists:
                    merged.education.append(edu)

            # ------------------------------------------------
            # Experience
            # ------------------------------------------------
            for exp in candidate.experience:

                exists = any(
                    e.company == exp.company
                    and e.title == exp.title
                    for e in merged.experience
                )

                if not exists:
                    merged.experience.append(exp)

            # ------------------------------------------------
            # Provenance
            # ------------------------------------------------
            for prov in candidate.provenance:

                exists = any(
                    p.field == prov.field
                    and p.source == prov.source
                    for p in merged.provenance
                )

                if not exists:
                    merged.provenance.append(prov)

        return merged