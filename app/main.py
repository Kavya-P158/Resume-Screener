from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from app.parseFile import parse_pdf
from app.src.agents.resume_extractor_agent import resume_extractorFn
from app.src.agents.jd_extractor_agent import jd_extractorFn
from app.src.agents.candidate_evaluation_agent import candidate_evaluation
import json
 
app=FastAPI()

@app.post("/processResume")
async def analyse_resume(resume:UploadFile,jd:UploadFile):
    resumeTxt= parse_pdf(resume.file)

    #jdTxt=parse_pdf("app/src/resources/job_description.pdf")
    jdTxt=parse_pdf(jd.file)
    resume_extractResult=resume_extractorFn(resumeTxt)
    print(resume_extractResult)

    cleaned_result = resume_extractResult.replace("```json", "").replace("```", "").strip()
    print(cleaned_result)
    print(repr(cleaned_result))
    resume_Result=json.loads(cleaned_result)


    
    JDResponsefromLLM= jd_extractorFn(jdTxt)
    cleaned_result_jd = JDResponsefromLLM.replace("```json", "").replace("```", "").strip()
    jd_Result=json.loads(cleaned_result_jd)

    Candidate_Result=candidate_evaluation(resume_Result,jd_Result).replace("```json", "").replace("```", "").strip()
    Candidate_Result_json=json.loads(Candidate_Result)
    print(Candidate_Result_json)
    return JSONResponse(content=Candidate_Result_json)
