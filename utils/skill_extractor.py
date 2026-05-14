# utils/skill_extractor.py

import re

# Predefined skill database (you can expand this anytime)
SKILL_DB = [
    "python", "java", "c++", "c", "sql",
    "machine learning", "deep learning", "nlp",
    "data analysis", "data science",
    "pandas", "numpy", "matplotlib",
    "tensorflow", "keras", "scikit-learn",
    "excel", "power bi", "tableau",
    "html", "css", "javascript",
    "django", "flask", "streamlit",
    "git", "github"
]


def clean_text(text):
    """
    Clean and normalize resume text
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9+#. ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_skills(text):
    """
    Extract skills from resume text using keyword matching
    (Lightweight alternative to spaCy)
    """

    if not text:
        return []

    text = clean_text(text)

    found_skills = []

    for skill in SKILL_DB:
        # match whole words or phrases
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def match_skills(resume_skills, job_skills):
    """
    Compare resume skills with job description skills
    Returns match percentage
    """

    if not job_skills:
        return 0

    resume_set = set([s.lower() for s in resume_skills])
    job_set = set([s.lower() for s in job_skills])

    matched = resume_set.intersection(job_set)

    score = (len(matched) / len(job_set)) * 100

    return round(score, 2)