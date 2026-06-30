from src.models import Candidate


class ConfidenceScorer:
    """
    Computes an overall confidence score for a candidate profile.
    """

    def score(self, candidate: Candidate) -> float:

        score = 0.0

        # Required fields
        if candidate.full_name:
            score += 0.15

        if candidate.emails:
            score += 0.15

        if candidate.phones:
            score += 0.10

        if candidate.skills:
            score += 0.20

        if candidate.education:
            score += 0.15

        if candidate.experience:
            score += 0.15

        # Bonus for multiple sources
        sources = set()

        for skill in candidate.skills:
            sources.update(skill.sources)

        if len(sources) >= 2:
            score += 0.10

        candidate.overall_confidence = round(min(score, 1.0), 2)

        return candidate.overall_confidence