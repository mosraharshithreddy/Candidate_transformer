import pdfplumber
from pathlib import Path


class PDFParser:
    """
    Reads a PDF resume and extracts raw text.
    """

    def parse(self, file_path: str) -> str:
        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(f"PDF file not found: {file_path}")

        text = []

        try:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)

        except Exception as e:
            raise ValueError(f"Unable to read PDF: {e}")

        return "\n".join(text)