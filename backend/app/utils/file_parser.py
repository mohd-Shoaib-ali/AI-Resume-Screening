import fitz
import docx2txt
import os
import re

def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    name = filename.lower()

    if name.endswith(".pdf"):
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = "\n".join(page.get_text() for page in doc)
        return text

    if name.endswith(".docx"):
        temp_name = "temp_upload.docx"
        with open(temp_name, "wb") as f:
            f.write(file_bytes)
        text = docx2txt.process(temp_name) or ""
        os.remove(temp_name)
        return text

    return file_bytes.decode("utf-8", errors="ignore")

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()