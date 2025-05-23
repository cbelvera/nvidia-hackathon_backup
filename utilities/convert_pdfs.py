import os
import fitz
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Define input and output folders
input_root = os.path.join("data", "input")
output_root = os.path.join("data", "output")

# Create output directory if it doesn't exist
os.makedirs(output_root, exist_ok=True)

def extract_text_with_ocr(pdf_path):
    text = ""
    images = convert_from_path(pdf_path)
    for image in images:
        text += pytesseract.image_to_string(image, lang='spa') + "\n"
    return text

def convert_pdf(pdf_path, txt_path):
    print(f"Processing:{pdf_path}")
    try:
        doc = fitz.open(pdf_path)
        text = "".join(page.get_text() for page in doc)

        used_ocr = False

        if not text.strip():
            print("No extractable text. Using OCR...")
            text = extract_text_with_ocr(pdf_path)
            used_ocr = True

        os.makedirs(os.path.dirname(txt_path), exist_ok=True)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved to: {txt_path}")
        return used_ocr

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return False

# Process all PDF files in the subfolders
processed_files = 0
ocr_files = 0

for root, _, files in os.walk(input_root):
    for file in files:
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(root,file)
            relative_path = os.path.relpath(pdf_path, input_root)
            txt_path = os.path.join(output_root, os.path.splitext(relative_path)[0] + ".txt")

            used_ocr = convert_pdf(pdf_path, txt_path)

            processed_files += 1
            if used_ocr:
                ocr_files += 1

# Summary log
print(f"\n Extracted text from {processed_files} PDF files.")
print(f"OCR used in {ocr_files} files.")