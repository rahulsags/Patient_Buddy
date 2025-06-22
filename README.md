# Patient Buddy

**A Medical Document Analyzer and Assistant**

Patient Buddy helps users understand their medical test results by extracting key parameters from health documents and providing personalized explanations through a conversational interface — all while keeping your data private and local.

---

## Features

- **Document Processing**: Extract medical parameters from PDFs and images using advanced text extraction techniques (OCR)
- **Parameter Identification**: Automatically detect and normalize medical test values and their units
- **Abnormality Detection**: Identify out-of-range values based on established medical references
- **Personalized Explanations**: Get simple, clear explanations of your test results through a conversational assistant
- **Privacy-Focused**: All processing happens locally on your machine — no data is sent to external servers

---

## Installation

Follow these steps to set up **Patient Buddy** locally:


Clone the repository
```
git clone https://github.com/yourusername/Patient_Buddy_Local.git
cd Patient_Buddy_Local
```
Create and activate a virtual environment
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
Install required packages
```
pip install -r requirements.txt
```
## Local LLM Setup with Ollama
This project uses Ollama for running lightweight local language models.

1. Install Ollama  
```
Follow instructions at: https://ollama.ai/download
```
2. Pull the required model
```
ollama pull tinyllama
```

## Run the application
```
python run.py
```

## Technical Details

OCR Engine: Tesseract OCR + pdf2image

LLM: TinyLlama via Ollama for local inference

Text Processing: Pattern matching and value normalization for medical parameter extraction

Explanation Engine: Hybrid system with rule-based logic and LLM-based fallback for robust response generation

## Privacy & Limitations

- All document processing and inference happen entirely on your local machine

- This tool is not a substitute for professional medical advice

- Accuracy may vary depending on:

  - Document quality (image resolution, clarity, layout)

  - OCR performance

  - LLM limitations and training data

