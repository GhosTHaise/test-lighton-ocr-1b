import ollama
import pypdfium2 as pdfium
import requests
from io import BytesIO

# Download PDF from arXiv
pdf_url = "https://arxiv.org/pdf/2412.13663"
pdf_data = requests.get(pdf_url).content

# Open PDF and convert first page to image
pdf = pdfium.PdfDocument(pdf_data)
page = pdf[0]

# Render at 200 DPI (scale factor = 200/72 ≈ 2.77)
pil_image = page.render(scale=2.77).to_pil()

# Convert to base64
buffer = BytesIO()
pil_image.save(buffer, format="PNG")
image_bytes = buffer.getvalue()


res = ollama.chat(
    model='maternion/LightOnOCR-2',
    messages=[{
        'role': 'user',
        'content': 'Please extract all the text from this document and format it as JSON.',
        'images': [image_bytes] # Pass the bytes directly here
    }]
)

print(res['message']['content'])