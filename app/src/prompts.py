EXTRACT_CANDIDATE_DETAILS = """
You are an expert in resume screening. Your task is to extract relevant details from a resume.
You will receive a resume in text format, and you need to identify key information such as:
- name (string)
- email (string)
- phone (string)
- education (string or null)
- work_experience (integer or null)
- skills (list of strings)
- certifications (list of strings)

Your response must be a valid JSON object.
Use `null` if a value is missing.
Do NOT fabricate or infer information.
Only extract values explicitly present in the resume.
If information is missing, return null.
Do not provide any justification if value is missing , provide the value as null

Here is the resume text:
{resume_text}

Expected response format:
{{
  "name": "John Doe",
  "email": "abc@gmail.com",
  "phone": "1234567890",
  "education": "Bachelor of Science in Computer Science",
  "work_experience": 7,
  "skills": ["Python", "FastAPI", "Machine Learning"],
  "certifications": ["Certified Python Developer"]
}}
"""
EXTRACT_JD_DETAILS="""
You are an expert in filtering the required skills and experience from a given job description. Your task is to extract relevant details from a resume.
You will receive the job description in text format, and you need to identify key information such as:
- min_work_experience in years (integer or null)
- max_work_experience in years (integer or null)
- skills (list of strings)

Your response must be a valid JSON object.
Use `null` if a value is missing.
If experience is not avaialble as a range, for example, "5+ years", consider it as 5 for min_work_experience and 8 for max_work_experience (assuming +3 years as the maximum).

Here is the job description text:
{jd_text}

Expected response format:
{{
  "min_work_experience": 7,
  "max_work_experience": 10,
  "skills": ["Python", "FastAPI", "Machine Learning"]
}}


"""
CANDIDATE_EVALUATION="""
You are a candidate evaluation agent. You will be given two inputs. 
1.Candidate's profile (json format)
2.Job description (json format)

Your task is to compare both the data and provide the following as output:
1.Whether at least 50% of the required skills are present.
2.Whether the work experience is within the acceptable range. This should be between the min_work_experience and max_work_experience from the job description with a tolerance of +/- 2 years. Anyhing outside this range should be considered a mismatch and the candidate should be rejected


If both the Condition 1 and condition 2 are true return the status as selected . If not, return as Rejected.
While matching skills, consider the following:
    - If the skills are related to the job description. For example, if the job description requires CI/CD and the candidate has DevOps experience, consider it a match.
You should provide the output in below JSON format
{{
  "candidate_status": "Selected" or "Rejected",
  "reason": "Explain the decision in detail with clarity in minimum of two or three sentences. Focus on the skills of the candidate and the experiences.",
  "matched_skills": [...],
  "skill_match_percentage": 68,
  "experience": 5
}}

Here is the input data:
CAndidate profile:{candidate_data}
Job description:{jd_data}
"""