JOB_DATABASE = {

    "Data Scientist": [
        "python",
        "machine learning",
        "sql",
        "data science"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react"
    ],

    "Backend Developer": [
        "python",
        "fastapi",
        "django",
        "flask",
        "sql"
    ],

    "Full Stack Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "python",
        "sql"
    ],

    "AI Engineer": [
        "python",
        "machine learning",
        "deep learning"
    ]
}

def recommend_jobs(skills):

    recommended_jobs = []

    for job, required_skills in JOB_DATABASE.items():

        match_count = 0

        for skill in skills:

            if skill in required_skills:
                match_count += 1

        if match_count >= 2:
            recommended_jobs.append(job)

    return recommended_jobs