from src.github.github_client import GitHubClient

client = GitHubClient()

# Replace with your actual GitHub username if different
profile = client.fetch("HarshithReddy")

print("=" * 50)
print("GitHub Skills")
print("=" * 50)

print(profile["skills"])