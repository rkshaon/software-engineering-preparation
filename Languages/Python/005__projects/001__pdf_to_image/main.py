from pdf2image import convert_from_path

import os

# Get project directory
file_name = "backend.pdf"
file_directory = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), file_name)

# Convert each page of the PDF to an image
pages = convert_from_path(file_directory, dpi=300)
for page in pages:
    page.save(file_name.replace(".pdf", "") +
              ".jpg", "JPEG")
