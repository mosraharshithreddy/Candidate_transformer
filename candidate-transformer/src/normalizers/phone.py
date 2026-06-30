import phonenumbers
from phonenumbers import PhoneNumberFormat


def normalize_phone(phone: str) -> str | None:
    """
    Normalize a phone number to E.164 format.
    Returns None if invalid.
    """

    if not phone:
        return None

    phone = phone.strip()

    try:
        parsed = phonenumbers.parse(phone, "IN")

        if not phonenumbers.is_valid_number(parsed):
            return None

        return phonenumbers.format_number(
            parsed,
            PhoneNumberFormat.E164
        )

    except Exception:
        return None