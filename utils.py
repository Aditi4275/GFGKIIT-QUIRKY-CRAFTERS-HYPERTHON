import base64
import io
import re
import fitz  # PyMuPDF
from PIL import Image
import google.generativeai as genai

def get_gemini_response(input, pdf_content, prompt):
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf_doc:
            first_page = pdf_doc[0].get_pixmap()
            img_byte_arr = io.BytesIO(first_page.tobytes("jpeg"))
            return Image.open(img_byte_arr), base64.b64encode(img_byte_arr.getvalue()).decode()
    else:
        raise FileNotFoundError("No file uploaded")

def extract_match_percentage(response_text):
    match = re.search(r"Match Percentage:\s*(\d+)%", response_text)
    return int(match.group(1)) if match else 0

