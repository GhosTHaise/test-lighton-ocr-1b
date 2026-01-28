import ollama
import pypdfium2 as pdfium
import requests
from io import BytesIO
import json

# Download PDF from arXiv
pdf_url = "https://arxiv.org/pdf/2412.13663"
pdf_data = requests.get(pdf_url).content

# Open PDF
pdf = pdfium.PdfDocument(pdf_data)

# This list will hold the JSON results from each page
all_pages_data = []

print(f"Starting OCR for {len(pdf)} pages...")

# Loop through every page in the PDF
for i, page in enumerate(pdf):
    print(f"Processing page {i + 1}...")
    
    # Render page to image (200 DPI)
    pil_image = page.render(scale=2.77).to_pil()

    # Convert image to bytes
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()

    # Send to Ollama
    res = ollama.chat(
        model='maternion/LightOnOCR-2',
        messages=[{
            'role': 'user',
            'content': 'Please extract all the text from this document and format it as JSON.',
            'images': [image_bytes]
        }]
    )

    # Store the content
    # Note: You might want to try-except this if the model returns non-JSON text
    page_content = res['message']['content']
    all_pages_data.append({
        "page": i + 1,
        "content": page_content
    })

# Final output: list of all page extractions
full_document_json = json.dumps(all_pages_data, indent=4)
print("--- Extraction Complete ---")
print(full_document_json)