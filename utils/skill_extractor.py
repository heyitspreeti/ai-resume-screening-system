
import spacy

# ==========================
# LOAD NLP MODEL
# ==========================

nlp = spacy.load("en_core_web_sm")

# ==========================
# SKILL DATABASE
# ==========================

SKILLS = [

    "python",
    "java",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "machine learning",
    "deep learning",
    "data science",
    "fastapi",
    "streamlit",
    "django",
    "flask",
    "mongodb",
    "mysql",
    "git",
    "github"

]

# ==========================
# NLP SKILL EXTRACTION
# ==========================

def extract_skills(resume_text):

    doc = nlp(resume_text.lower())

    detected_skills = []

    for token in doc:

        for skill in SKILLS:

            if skill.lower() in token.text.lower():

                if skill not in detected_skills:
                    detected_skills.append(skill)

    # ==========================
    # CHECK MULTI-WORD SKILLS
    # ==========================

    for skill in SKILLS:

        if " " in skill:

            if skill.lower() in resume_text.lower():

                if skill not in detected_skills:
                    detected_skills.append(skill)

    return detected_skills

