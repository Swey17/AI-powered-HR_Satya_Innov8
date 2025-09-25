# CODE TO CONVERT ALL PDF RESUMES TO TXT FILES

from pypdf import PdfReader # to read pdf files
from tqdm import tqdm # for progress bar

# Function to convert PDF to text
def pdf_to_text(file_path):
    reader = PdfReader(file_path)

    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    return full_text

for i in tqdm(range(1000)):
    try:
        file_path = f"Final_resumes_pdf/Resume_of_ID_{i}.pdf"
        text = pdf_to_text(file_path)

        # write in Final_resumes_txt folder
        with open(f"Final_resumes_txt/Resume_of_ID_{i}.txt", "w", encoding="utf-8") as text_file:
            text_file.write(text)

    except Exception as e: # to handle cases where the PDF might be corrupted or missing
        print(f"Failed to convert Resume_of_ID_{i}.pdf: {e}")