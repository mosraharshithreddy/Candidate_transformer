from src.normalizers.skill import normalize_skill

skills = [
    "Javascript",
    "js",
    "React",
    "React.js",
    "ML",
    "machine learning",
    "NLP",
    "Git hub",
    "Python",
    "",
    None
]

for skill in skills:
    print(skill, "->", normalize_skill(skill))