import ollama
import requests
from io import BytesIO

# 1. The image URL
url = "https://huggingface.co/datasets/hf-internal-testing/fixtures_ocr/resolve/main/SROIE-receipt.jpeg"

# 2. Download the image into memory
response = requests.get(url)
if response.status_code == 200:
    image_bytes = response.content
    
    # 3. Use Ollama to process the OCR task
    # Note: Ensure you have a vision-capable model pulled (e.g., 'llama3.2-vision' or 'llava')
    res = ollama.chat(
        model='maternion/LightOnOCR-2',
        messages=[{
            'role': 'user',
            'content': 'Please extract all the text from this receipt and format it as JSON.',
            'images': [image_bytes]
        }]
    )

    print(res['message']['content'])
else:
    print("Failed to retrieve the image.")