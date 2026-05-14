
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ======================================
# TRAINING DATA
# ======================================

training_resumes = [

    # DATA SCIENCE

    "python machine learning data analysis pandas numpy sql",

    "deep learning tensorflow python ai data science",

    "machine learning python statistics sql",

    # WEB DEVELOPMENT

    "html css javascript react frontend web design",

    "react node.js javascript frontend developer",

    "html css bootstrap web application",

    # BACKEND DEVELOPMENT

    "python fastapi flask django backend api sql",

    "backend developer sql database fastapi",

    "django flask rest api backend",

    # AI ENGINEER

    "artificial intelligence deep learning python neural networks",

    "nlp machine learning ai engineer python",

    "computer vision deep learning tensorflow"

]

training_labels = [

    "Data Science",
    "Data Science",
    "Data Science",

    "Web Development",
    "Web Development",
    "Web Development",

    "Backend Development",
    "Backend Development",
    "Backend Development",

    "AI Engineer",
    "AI Engineer",
    "AI Engineer"

]

# ======================================
# VECTORIZATION
# ======================================

vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(
    training_resumes
)

# ======================================
# MODEL TRAINING
# ======================================

model = MultinomialNB()

model.fit(
    X_train,
    training_labels
)

# ======================================
# PREDICTION FUNCTION
# ======================================

def predict_resume_category(resume_text):

    resume_vector = vectorizer.transform(
        [resume_text]
    )

    prediction = model.predict(
        resume_vector
    )

    return prediction[0]
