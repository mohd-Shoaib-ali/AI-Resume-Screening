import streamlit as st
import requests

API = st.sidebar.text_input("API URL", "http://localhost:8000")

st.title("AI Resume Screening Platform")

tab1, tab2, tab3, tab4 = st.tabs(["Upload Resume", "Create Job", "Match", "History"])

with tab1:
    name = st.text_input("Candidate Name")
    email = st.text_input("Email")
    file = st.file_uploader("Resume PDF/DOCX")
    if st.button("Upload Resume") and file:
        files = {"file": (file.name, file.getvalue(), file.type)}
        r = requests.post(
        f"{API}/resumes/upload",
            data={
            "name": name,
            "email": email
        },
    files=files
)
        st.json(r.json())

with tab2:
    title = st.text_input("Job Title")
    desc = st.text_area("Job Description")
    if st.button("Create Job"):
        r = requests.post(f"{API}/jobs/", json={"title": title, "description": desc})
        st.json(r.json())

with tab3:
    resume_id = st.number_input("Resume ID", min_value=1, step=1)
    job_id = st.number_input("Job ID", min_value=1, step=1)
    if st.button("Run Match"):
        r = requests.post(f"{API}/matches/", json={"resume_id": int(resume_id), "job_id": int(job_id)})
        st.json(r.json())

with tab4:
    if st.button("Load History"):
        r = requests.get(f"{API}/matches/")
        st.json(r.json())