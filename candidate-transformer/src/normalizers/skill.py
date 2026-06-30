SKILL_ALIASES = {
    "javascript": "JavaScript",
    "js": "JavaScript",

    "ml": "Machine Learning",
    "machine learning": "Machine Learning",

    "nlp": "Natural Language Processing",
    "natural language processing": "Natural Language Processing",

    "github": "GitHub",
    "git hub": "GitHub",

    "react": "React.js",
    "reactjs": "React.js",
}


def normalize_skill(skill: str) -> str | None:
    """
    Normalize a skill name.
    """

    if not skill:
        return None

    skill = skill.strip()

    if not skill:
        return None

    key = skill.lower()

    return SKILL_ALIASES.get(key, skill)