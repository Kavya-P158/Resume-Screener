import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")
st.title("Resume screening app")

uploaded_file=st.file_uploader("Upload a resume",type="pdf")
jd_file=st.file_uploader("Upload a job description",type="pdf")
if uploaded_file and jd_file is not None:
    print(uploaded_file)
    st.write("Files uploaded successfully")
    print("File uploaded successfully",uploaded_file.name)
    if st.button("Process resume"):
        response=requests.post(f"{API_URL}/processResume",
                               files={"resume":uploaded_file,"jd":jd_file})
        if(response.status_code==200):
            response_data=response.json()
            print(type(response_data))
            print(response_data)
            st.write("Candidate Status ",response_data["candidate_status"])
            st.write("Feedback ",response_data["reason"])
            st.write("Skills matched ",response_data["matched_skills"])
            st.write("Experience ",response_data["experience"])
            st.write("Skills match percentage ",response_data["skill_match_percentage"])

