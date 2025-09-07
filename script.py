import os
import cv2
import pytesseract
import pandas as pd
from pdf2image import convert_from_path

# Define the static directory path
STATIC_PATH = "/home/rushikeshw@rhythm.local/Desktop/pan"

def extract_text_from_image(image_path):
    """Extract text from an image using Tesseract OCR."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray)  # Extract text
    return text

def extract_text_from_pdf(pdf_path):
    """Convert PDF to images and extract text from each page."""
    images = convert_from_path(pdf_path)  # Convert PDF to image
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        full_text += text + "\n"
    return full_text

def parse_pan_card_text(text):
    """Extract PAN details from text."""
    lines = text.split("\n")
    pan_number, name = None, None
    for line in lines:
        line = line.strip()
        if len(line) == 10 and line.isalnum():  # PAN number format
            pan_number = line
        elif name is None and line.isalpha():  # Extracting Name (first occurrence)
            name = line

    return name, pan_number

def save_to_excel(data, filename="pan_details.xlsx"):
    """Save extracted details to an Excel file."""
    df = pd.DataFrame(data, columns=["Sr No", "Name", "PAN Number"])
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

def process_file(file_path, sr_no):
    """Process an image or PDF file to extract PAN details and return data."""
    ext = os.path.splitext(file_path)[-1].lower()
    if ext in [".jpg", ".jpeg", ".png"]:
        text = extract_text_from_image(file_path)
    elif ext in [".pdf"]:
        text = extract_text_from_pdf(file_path)
    else:
        print(f"Unsupported file format: {file_path}")
        return None

    name, pan_number = parse_pan_card_text(text)
    if name and pan_number:
        return (sr_no, name, pan_number)
    else:
        print(f"PAN details not found in {file_path}")
        return None

# Main function to process all files in STATIC_PATH
def process_all_files(directory):
    data = []
    sr_no = 1

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file
            record = process_file(file_path, sr_no)
            if record:
                data.append(record)
                sr_no += 1  # Increment serial number

    if data:
        save_to_excel(data)
    else:
        print("No valid PAN data extracted!")

# Run the function
process_all_files(STATIC_PATH)
