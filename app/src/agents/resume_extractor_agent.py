from dotenv import load_dotenv
from openai import OpenAI
import os
import json
from app.src.prompts import EXTRACT_CANDIDATE_DETAILS
from google import genai

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def resume_extractorFn(resumeTxt):

    prompt=EXTRACT_CANDIDATE_DETAILS.format(resume_text=resumeTxt)
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print("RESPONSE FROM LLM IS BELOW")
    print(response.text)
    return response.text
