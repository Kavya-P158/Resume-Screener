from google import genai
from openai import OpenAI
from app.src.prompts import EXTRACT_JD_DETAILS
import os
from dotenv import load_dotenv

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def jd_extractorFn(jdFileTxt):
    prompt=EXTRACT_JD_DETAILS.format(jd_text=jdFileTxt)
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
#     client = OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="ollama"
# )
#     response = client.chat.completions.create(
#     model="mistral:latest",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )
#     print(response.choices[0].message.content)
#     return response.choices[0].message.content

