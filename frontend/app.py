
import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

# ===================================
# IMPORT UTILITIES
# ===================================

from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_calculator import calculate_ats_score
from utils.job_recommender import recommend_jobs
from utils.report_generator import generate_report
from utils.database import save_resume_data, fetch_all_data
from utils.semantic_matcher import calculate_similarity
from utils.resume_classifier import predict_resume_category

# ===================================
# PAGE CONFIG
# ===================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ===================================
# TITLE
# ===================================

st.title("📄 AI Resume Screening System")

st.sidebar.title("Navigation")

st.sidebar.write("AI Resume Analyzer Dashboard")

# ===================================
# FILE UPLOAD
# ===================================

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# ===================================
# JOB DESCRIPTION INPUT
# ===================================

job_description = st.text_area(
    "Paste Job Description"
)

# ===================================
# MAIN APPLICATION LOGIC
# ===================================

if uploaded_file:

    st.success("Resume Uploaded Successfully")

    # ===================================
    # EXTRACT RESUME TEXT
    # ===================================

    resume_text = extract_text_from_pdf(
        uploaded_file
    )

    # ===================================
    # EXTRACT SKILLS
    # ===================================

    skills = extract_skills(
        resume_text
    )

    # ===================================
    # ATS SCORE
    # ===================================

    ats_score = calculate_ats_score(
        skills
    )

    # ===================================
    # JOB RECOMMENDATIONS
    # ===================================

    recommended_jobs = recommend_jobs(
        skills
    )

    # ===================================
    # SEMANTIC MATCH SCORE
    # ===================================

    similarity_score = 0

    if job_description:

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

    # ===================================
    # ML RESUME CATEGORY PREDICTION
    # ===================================

    predicted_category = predict_resume_category(
        resume_text
    )

    # ===================================
    # SAVE TO DATABASE
    # ===================================

    save_resume_data(
        uploaded_file.name,
        skills,
        ats_score,
        recommended_jobs
    )

    # ===================================
    # DASHBOARD METRICS
    # ===================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Skills Detected",
        len(skills)
    )

    col2.metric(
        "ATS Score",
        f"{ats_score}%"
    )

    col3.metric(
        "Recommended Jobs",
        len(recommended_jobs)
    )

    st.divider()

    # ===================================
    # VIEW RESUME TEXT
    # ===================================

    with st.expander("View Resume Text"):

        st.write(resume_text)

    st.divider()

    # ===================================
    # DETECTED SKILLS
    # ===================================

    st.subheader("✅ Detected Skills")

    for skill in skills:

        st.write("✔️", skill)

    st.divider()

    # ===================================
    # ATS SCORE DISPLAY
    # ===================================

    st.subheader("📊 ATS Resume Score")

    st.progress(
        int(ats_score)
    )

    st.write(
        f"Resume Score: {ats_score}%"
    )

    st.divider()

    # ===================================
    # SEMANTIC MATCH SCORE
    # ===================================

    st.subheader("🧠 Resume-Job Match Score")

    st.progress(
        int(similarity_score)
    )

    st.write(
        f"Match Score: {similarity_score}%"
    )

    st.divider()

    # ===================================
    # ML CATEGORY PREDICTION
    # ===================================

    st.subheader("🤖 Predicted Resume Category")

    st.success(
        predicted_category
    )

    st.divider()

    # ===================================
    # JOB RECOMMENDATIONS
    # ===================================

    st.subheader("💼 Recommended Jobs")

    for job in recommended_jobs:

        st.write("➡️", job)

    st.divider()

    # ===================================
    # SKILL ANALYTICS CHART
    # ===================================

    st.subheader("📈 Skill Analytics")

    if skills:

        skill_data = pd.DataFrame({

            "Skill": skills,

            "Count": [1] * len(skills)

        })

        fig, ax = plt.subplots()

        ax.pie(

            skill_data["Count"],

            labels=skill_data["Skill"],

            autopct='%1.1f%%'

        )

        st.pyplot(fig)

    st.divider()

    # ===================================
    # PDF REPORT GENERATION
    # ===================================

    st.subheader("📄 Download Analysis Report")

    report_file = "resume_report.pdf"

    generate_report(

        report_file,

        skills,

        ats_score,

        recommended_jobs

    )

    with open(report_file, "rb") as pdf_file:

        st.download_button(

            label="Download Report",

            data=pdf_file,

            file_name="AI_Resume_Report.pdf",

            mime="application/pdf"

        )

    st.divider()

    # ===================================
    # DATABASE RECORDS
    # ===================================

    st.subheader("🗂 Previous Resume Analyses")

    all_data = fetch_all_data()

    if all_data:

        data_frame = pd.DataFrame(

            all_data,

            columns=[

                "ID",

                "File Name",

                "Skills",

                "ATS Score",

                "Recommended Jobs"

            ]
        )

        st.dataframe(
            data_frame
        )

