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

1. Summary of Inspection
2. Detected Defects
3. Severity Level (Low / Medium / High)
4. Possible Causes
5. Recommended Maintenance or Repair Actions
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content