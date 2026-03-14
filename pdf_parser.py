import pdfplumber
import fitz
import os

def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def extract_images(pdf_file, output_folder="images"):
    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    image_paths = []

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)

        pix = page.get_pixmap(matrix=fitz.Matrix(2,2))  # better quality
        image_path = f"{output_folder}/page_{page_index}.png"

        pix.save(image_path)
        image_paths.append(image_path)

    return image_paths