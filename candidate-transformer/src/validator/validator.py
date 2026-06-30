from src.models import Candidate


class CandidateValidator:
    """
    Validate the final merged candidate.
    """

    def validate(self, candidate: Candidate):

        errors = []

        # Required fields
        if not candidate.full_name:
            errors.append("Missing full name.")

        if not candidate.emails:
            errors.append("Missing email.")

        if not candidate.phones:
            errors.append("Missing phone.")

        # Duplicate emails
        if len(candidate.emails) != len(set(candidate.emails)):
            errors.append("Duplicate emails found.")

        # Duplicate phones
        if len(candidate.phones) != len(set(candidate.phones)):
            errors.append("Duplicate phone numbers found.")

        # Duplicate skills
        skill_names = [skill.name.lower() for skill in candidate.skills]

        if len(skill_names) != len(set(skill_names)):
            errors.append("Duplicate skills found.")

        return errors