import fitz
import os


def extract_text(file_path):
    return


# Get the current file's directory
current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = "resource/demo.pdf"
file_directory = os.path.join(current_directory, file_name)
print(file_directory)
text = extract_text(file_path=file_directory)

print(text)
