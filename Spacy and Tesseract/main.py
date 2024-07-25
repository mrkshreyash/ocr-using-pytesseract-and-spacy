import json
from PIL import Image
import pytesseract

def ocr_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Use Tesseract OCR to extract text
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text

def extract_key_value_pairs(text):
    key_value_pairs = {}

    # Split the text into lines
    lines = text.split('\n')

    current_key = None
    current_value = ""

    for line in lines:
        # Split each line into words
        words = line.split()

        # Assuming a simple key-value structure like "Key: Value"
        if len(words) >= 2:
            current_key = words[0]
            current_value = ' '.join(words[1:])
            key_value_pairs[current_key] = current_value
        elif current_key is not None:
            current_value += ' ' + line.strip()
            key_value_pairs[current_key] = current_value

    return key_value_pairs

if __name__ == "__main__":
    # Replace 'your_invoice_image.png' with the path to your invoice image
    image_path = 'sample2.jpg'

    # Perform OCR on the image
    extracted_text = ocr_image(image_path)

    # Extract key-value pairs
    key_value_pairs = extract_key_value_pairs(extracted_text)

    # Write key-value pairs to a JSON file
    with open("Invoice.json", "w") as json_file:
        json.dump(key_value_pairs, json_file, indent=4)

