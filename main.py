import fitz  # PyMuPDF
import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\moham\Documents\Tesseract-OCR\tesseract.exe'

from PIL import Image
import os


# Function to convert PDF to images
def pdf_to_images(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()  # Render page to image
        img_path = f"page_{page_num}.png"
        pix.save(img_path)
        images.append(img_path)
    return images


# Function to perform OCR on images
def ocr_on_images(image_paths):
    text = ""
    for image_path in image_paths:
        img = Image.open(image_path)
        text += pytesseract.image_to_string(img)
    return text


# Function to convert PDF to text
def pdf_to_text(pdf_path, output_txt_path):
    # Convert PDF to images
    image_paths = pdf_to_images(pdf_path)

    # Perform OCR on the images
    text = ocr_on_images(image_paths)

    # Write the extracted text to a file
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Clean up image files
    for img_path in image_paths:
        os.remove(img_path)

# Function to select file path
def select_file():
    # Hide the root window
    Tk().withdraw()

    # Open file explorer and get the selected file's path
    file_path = askopenfilename(
        title="Select an image file",
        filetypes=[("PDF files", "*.pdf")]
    )
    return file_path

# Function to process file name for output text
def get_output_filename(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]  # Get file name without extension
    output_file_name = f"{base_name}_converted_to_text.txt"  # Add suffix and file extension
    return os.path.join(os.path.dirname(file_path), output_file_name)


# Use the file explorer to select an image file
image_path = select_file()
print("")
output_file = get_output_filename(select_file())
pdf_to_text(select_file(), output_file)
print(f"Text extracted and saved to {output_file}")
