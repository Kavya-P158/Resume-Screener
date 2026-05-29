from PyPDF2 import PdfReader

def parse_pdf(file):
    print("FILE is",file)
    reader=PdfReader(file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text.strip()