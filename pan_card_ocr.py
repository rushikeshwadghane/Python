"""Extracts PAN-card text from user-selected images or PDFs and saves results."""

import argparse
import os

import cv2
import pandas as pd
import pytesseract
from pdf2image import convert_from_path


def extract_text_from_image(image_path):
    """Extract text from an image using Tesseract OCR."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Unable to read image: {image_path}")
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(grayscale)


def extract_text_from_pdf(pdf_path):
    """Convert PDF pages to images and extract their text."""
    images = convert_from_path(pdf_path)
    return "\n".join(pytesseract.image_to_string(image) for image in images)


def parse_pan_card_text(text):
    """Return the first plausible name and PAN-like identifier found in text."""
    lines = [line.strip() for line in text.splitlines()]
    pan_number = next(
        (line for line in lines if len(line) == 10 and line.isalnum()),
        None,
    )
    name = next(
        (line for line in lines if line.isalpha() and line != pan_number),
        None,
    )
    return name, pan_number


def save_to_excel(data, filename):
    """Save extracted records to a spreadsheet."""
    dataframe = pd.DataFrame(data, columns=["Serial number", "Name", "PAN number"])
    dataframe.to_excel(filename, index=False)
    print(f"Data saved to {filename}")


def process_file(file_path, serial_number):
    """Extract PAN-card fields from one supported image or PDF file."""
    extension = os.path.splitext(file_path)[-1].lower()
    if extension in {".jpg", ".jpeg", ".png"}:
        text = extract_text_from_image(file_path)
    elif extension == ".pdf":
        text = extract_text_from_pdf(file_path)
    else:
        print(f"Unsupported file format: {file_path}")
        return None

    name, pan_number = parse_pan_card_text(text)
    if name and pan_number:
        return serial_number, name, pan_number

    print(f"PAN details not found in {file_path}")
    return None


def process_all_files(directory, output_path):
    """Process supported files in a directory and write extracted records."""
    records = []
    for file_path in sorted(os.listdir(directory)):
        full_path = os.path.join(directory, file_path)
        if not os.path.isfile(full_path):
            continue
        record = process_file(full_path, len(records) + 1)
        if record:
            records.append(record)

    if records:
        save_to_excel(records, output_path)
    else:
        print("No valid PAN data extracted.")


def main():
    """Parse command-line paths and process the selected directory."""
    parser = argparse.ArgumentParser(
        description="Extract PAN-card text from image and PDF files."
    )
    parser.add_argument("directory", help="Directory containing local input files")
    parser.add_argument(
        "--output",
        default="pan_details.xlsx",
        help="Output spreadsheet path (default: pan_details.xlsx)",
    )
    args = parser.parse_args()
    process_all_files(args.directory, args.output)


if __name__ == "__main__":
    main()
