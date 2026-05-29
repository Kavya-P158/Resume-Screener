from google import genai
from openai import OpenAI
import os
from dotenv import load_dotenv
from app.src.prompts import CANDIDATE_EVALUATION

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def candidate_evaluation(resume_Result,jd_Result):
   prompt=CANDIDATE_EVALUATION.format(candidate_data=resume_Result,jd_data=jd_Result)
   response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
   return response.text
#    client = OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="ollama"
# )
#    response = client.chat.completions.create(
#     model="mistral:latest",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )
#    print(response.choices[0].message.content)
   #return response.choices[0].message.content