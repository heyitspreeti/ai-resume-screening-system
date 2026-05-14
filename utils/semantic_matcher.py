
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(
    resume_text,
    job_description
):

    text = [
        resume_text,
        job_description
    ]

    cv = CountVectorizer()

    matrix = cv.fit_transform(text)

    similarity_score = cosine_similarity(matrix)[0][1]

    return round(similarity_score * 100, 2)

