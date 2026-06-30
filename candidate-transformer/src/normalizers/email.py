import re


EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)


def normalize_email(email: str) -> str | None:
    """
    Normalize and validate an email address.

    Returns:
        normalized email or None
    """

    if not email:
        return None

    email = email.strip().lower()

    if not EMAIL_PATTERN.fullmatch(email):
        return None

    return email