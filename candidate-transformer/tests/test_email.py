from src.normalizers.email import normalize_email

emails = [
    " Harshith@gmail.com ",
    "HARSHITH@GMAIL.COM",
    "invalid-email",
    "",
    None,
]

for email in emails:
    print(email, "->", normalize_email(email))