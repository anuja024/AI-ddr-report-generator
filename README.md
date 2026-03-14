# AI DDR Report Generator

This project is an AI-powered system that automatically generates a **Defect Detection Report (DDR)** from inspection and thermal imaging reports.

### Live demo link
https://ai-ddr-report-generator.streamlit.app

## Features

- Upload inspection report (PDF)
- Upload thermal report (PDF)
- Extract observations using AI
- Identify defects and classify severity
- Determine possible causes
- Generate maintenance recommendations
- Extract thermal images
- Generate final DDR report in PDF format

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- pdfplumber
- FPDF
- Groq LLM API

## Workflow

1. Upload inspection report
2. Upload thermal report
3. Extract text and images from PDFs
4. AI analyzes inspection findings
5. Generate structured DDR report
6. Export final report as PDF

## Web Application


## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
