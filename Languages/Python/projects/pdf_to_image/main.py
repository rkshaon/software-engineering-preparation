from pdf2image import convert_from_path

import os


# Get the current file's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Navigate back four directories
previous_directory = current_directory
for _ in range(4):
    previous_directory = os.path.dirname(previous_directory)
roadmap_path = os.path.join(previous_directory, 'Roadmap/resources')

file_name = "mongodb.pdf"
file_directory = os.path.join(roadmap_path, file_name)

# Convert each page of the PDF to an image
pages = convert_from_path(file_directory, dpi=300)
for page in pages:
    page.save(file_name.replace(".pdf", "") +
              ".jpg", "JPEG")
