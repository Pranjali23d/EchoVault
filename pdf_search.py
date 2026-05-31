import os
from PyPDF2 import PdfReader

def search_pdfs(query):

    results = []

    pdf_folder = "data/reports"

    for filename in os.listdir(pdf_folder):

        if filename.endswith(".pdf"):

            path = os.path.join(pdf_folder, filename)

            try:
                reader = PdfReader(path)

                text = ""

                for page in reader.pages:
                    text += page.extract_text() or ""

                if query.lower() in text.lower():
                    results.append(filename)

            except Exception:
                pass

    return results
    