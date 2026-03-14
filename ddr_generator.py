from groq import Groq
import os

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

print(client.models.list())
def generate_ddr(inspection_text, thermal_text):

    prompt = f"""
    You are an engineering inspection assistant.

    Generate a detailed Defect Detection Report (DDR).
    Provide a severity table before listing detailed explanations.
    Also classify defects into Priority Level:
    Low / Medium / High / Critical
    Group observations by area (Hall, Bedroom, Kitchen etc.).

Inspection Notes:
{inspection_text}

Thermal Analysis:
{thermal_text}

Structure the report with the following sections:

1. Property Issue Summary
2. Area wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information (explicitly mention “Not Available” if needed)
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content