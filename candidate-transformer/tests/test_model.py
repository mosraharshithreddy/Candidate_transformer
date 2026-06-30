from src.models import Candidate

candidate = Candidate(candidate_id="CAND001")

print(candidate.model_dump_json(indent=4))