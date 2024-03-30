
"""img2text.ipynb
This is an Image to text project.

This code is not working due to unavalablity of "tesseract-ocr"
"""

import io

# !sudo apt install tesseract-ocr
# !pip install pytesseract

from PIL import Image
import pytesseract
import requests
from io import BytesIO


def load_image(image_url):
    if image_url.startswith("https://"):
        # Download the image from the URL
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
    else:
        # Assuming image_url is a local file path
        img = Image.open(image_url)
    return img

# Function to extract text from image URL
def extract_text_from_image_url(image_url):

    img = load_image(image_url)

    # Configure pytesseract to use the Google Colab Tesseract installation path
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    # Extract text from the image
    text = pytesseract.image_to_string(img)

    # Display the extracted text
    print(text)

# URL of the image
# image_url = "/content/drive/MyDrive/TextImg/sample.png"
# image_url = "/content/drive/MyDrive/TextImg/kangaroo-reading.jpg"
image_url = "https://replicate.delivery/pbxt/Jj87qg6dTft3R5kFIzda2vorF3epnzwJpv96PsKcgkdZipLV/figure-65.png"

# Call the function to extract text from the image URL
extract_text_from_image_url(image_url)