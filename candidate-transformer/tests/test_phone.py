from src.normalizers.phone import normalize_phone

phones = [
    "9704745443",
    "+91 9704745443",
    "97047-45443",
    "(97047)45443",
    "12345",
    "",
    None
]

for phone in phones:
    print(phone, "->", normalize_phone(phone))