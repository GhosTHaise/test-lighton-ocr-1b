

# test-lighton-ocr-1b 🚀

A lightweight, local OCR pipeline designed to convert PDF documents into structured JSON data. This project leverages the **LightOn-OCR-1B** model running on **Ollama** for high-accuracy text extraction without data leaving your machine.

## 🌟 Key Features

* **100% Local Inference:** Powered by Ollama, ensuring total data privacy.
* **Optimized Model:** Uses `maternion/LightOnOCR-2`, a vision-language model specialized in document text recognition.
* **Modern Python Tooling:** Powered by `uv` for lightning-fast dependency management and execution.

## 🛠️ Prerequisites

1. **Ollama** must be installed and running.
2. Pull the LightOnOCR model:
```bash
ollama pull maternion/LightOnOCR-2

```


3. **uv** installed on your system:
```bash
# Install uv via curl
curl -LsSf https://astral.sh/uv/install.sh | sh

```



## 🚀 Quick Start

Using `uv`, you don't need to manually manage virtual environments or install dependencies one by one.

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd test-lighton-ocr-1b

```


2. **Run the script**:
```bash
uv run main.py

```


*Note: `uv` will automatically handle dependencies (`ollama`, `pypdfium2`, `requests`, `pillow`) defined in the script or pyproject.toml.*

## 📝 How it Works

The pipeline follows these steps:

1. **Fetch**: Downloads the target PDF directly from a URL (e.g., an arXiv research paper).
2. **Render**: Converts PDF pages into high-resolution images (200 DPI) using `pypdfium2`.
3. **Process**: Sends the image bytes to the `LightOnOCR-2` vision model via Ollama's Chat API.
4. **Structure**: Aggregates the OCR results into a single, structured JSON object containing data for every page.

## 📊 Sample Output

```json
[
    {
        "page": 1,
        "content": "Full text extracted from page 1..."
    },
    {
        "page": 2,
        "content": "Full text extracted from page 2..."
    }
]

```

## ⚠️ Important Notes

* **Vision Resources:** While LightOn-OCR-1B is highly efficient, ensure your system has sufficient VRAM/RAM for smooth image processing.
* **Prompt Engineering:** The current prompt requests JSON format. Depending on the model's output, you might occasionally need to strip Markdown code blocks (e.g., `json ... `) from the response.

---
