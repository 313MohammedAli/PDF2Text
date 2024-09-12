
# PDF and Image to Text Converter Using OCR

This Python program allows you to convert **PDF** or **image** files into text using **Optical Character Recognition (OCR)**. It uses `Tesseract OCR` along with `PyMuPDF` to extract text from PDF files and `PIL` for image files. The program includes a graphical file explorer to select files and automatically processes them.

## Requirements

### 1. Tesseract OCR
To perform the OCR, you need to download and install **Tesseract OCR**. Please download it from the following link and install it in your **Documents** folder:
- [Download Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

### 2. Python Libraries
You will also need to install several Python libraries for this program to run.

### 3. Install Required Python Libraries
You can install the required libraries using `pip`:

```bash
pip install pytesseract Pillow PyMuPDF tkinter
```

### 4. Setting Up Tesseract Path
After installing Tesseract, if it's installed in the `Documents` folder (as recommended), update the path in the Python script. Find this line in the code:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\<Your-Username>\Documents\Tesseract-OCR\tesseract.exe'
```

Replace `<Your-Username>` with your actual username, or update the path based on your system.

## Usage

1. **Run the Python Script**:
   - Upon running the script, a file explorer window will pop up, allowing you to select either a **PDF** or **image** file.
   
2. **Supported File Types**:
   - **PDF Files**: The program will convert each page of the PDF into an image, then extract text using OCR.
   - **Image Files**: Supported image formats include `png`, `jpg`, `jpeg`, `bmp`, and `tiff`.

3. **Text Extraction**:
   - After selecting the file, the program will extract the text and display it in the console, as well as save the output text file using the original file name with the suffix `_converted_to_text`.

### Example Usage

```bash
python ocr_converter.py
```

Once the file explorer opens, select the file (PDF or image) you want to process. The program will then output the extracted text to the console and save it as a `.txt` file with the suffix `_converted_to_text`.

## Program Overview

Here’s a brief overview of how the program works:

1. **File Explorer**: The program uses the `tkinter` library to open a file dialog that allows users to select a file.
2. **OCR Process**:
   - **PDF Files**: Pages of the PDF are rendered as images using `PyMuPDF` (fitz), and then passed to Tesseract for text extraction.
   - **Image Files**: Directly processed using Tesseract.
3. **Text Output**: The extracted text is printed to the console and saved to a `.txt` file.

## Troubleshooting

### Access Denied Error
If you encounter an "Access Denied" error when trying to access the Tesseract executable, try running your Python script as an administrator, or move the Tesseract installation to a folder that does not require special permissions (such as `C:\Tesseract-OCR`).

### Tesseract Not Found
If you get an error like `TesseractNotFoundError`, make sure the path to `tesseract.exe` is correctly set in the script. If needed, adjust the `tesseract_cmd` variable to point to the correct path.

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Path\To\Tesseract-OCR\tesseract.exe'
```

## License

This project is licensed under the MIT License.
