import requests


class GitHubClient:
    """
    Fetch candidate information from the GitHub REST API.

    This client retrieves:
    - Profile information
    - Repository languages
    - Repository topics
    """

    BASE_URL = "https://api.github.com/users"

    def fetch(self, username: str) -> dict:

        username = username.strip()

        # Allow complete GitHub URL
        if username.startswith("https://github.com/"):
            username = username.rstrip("/").split("/")[-1]

        # -----------------------------
        # Profile
        # -----------------------------
        profile_url = f"{self.BASE_URL}/{username}"

        response = requests.get(
            profile_url,
            headers={
                "Accept": "application/vnd.github+json"
            },
            timeout=10,
        )

        if response.status_code == 404:
            raise ValueError(
                f"GitHub user '{username}' not found."
            )

        response.raise_for_status()

        profile = response.json()

        # -----------------------------
        # Repositories
        # -----------------------------
        repo_url = f"{profile_url}/repos"

        repo_response = requests.get(
            repo_url,
            headers={
                "Accept": "application/vnd.github+json"
            },
            timeout=10,
        )

        repo_response.raise_for_status()

        repos = repo_response.json()

        skills = set()

        projects = []

        for repo in repos:

            # Primary language
            language = repo.get("language")

            if language:
                skills.add(language)

            # Topics
            for topic in repo.get("topics", []):
                if topic:
                    skills.add(topic)

            # Repository summary
            projects.append(
                {
                    "name": repo.get("name"),
                    "description": repo.get("description"),
                    "language": language,
                    "url": repo.get("html_url"),
                }
            )

        return {
            "candidate_id": None,

            "full_name": profile.get("name"),

            "email": profile.get("email"),

            "phone": None,

            "headline": profile.get("bio"),

            "years_experience": None,

            "skills": sorted(skills),

            "location": profile.get("location"),

            "links": {
                "github": profile.get("html_url"),
                "portfolio": profile.get("blog"),
                "linkedin": None,
            },

            "projects": projects,

            "public_repos": profile.get("public_repos"),

            "followers": profile.get("followers"),

            "following": profile.get("following"),
        }