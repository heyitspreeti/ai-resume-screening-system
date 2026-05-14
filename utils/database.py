import sqlite3

# ==========================
# CONNECT DATABASE
# ==========================

conn = sqlite3.connect(
    "resume_data.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==========================
# CREATE TABLE
# ==========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS resume_analysis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    file_name TEXT,

    skills TEXT,

    ats_score REAL,

    recommended_jobs TEXT

)

""")

conn.commit()

# ==========================
# SAVE DATA
# ==========================

def save_resume_data(
    file_name,
    skills,
    ats_score,
    recommended_jobs
):

    cursor.execute("""

    INSERT INTO resume_analysis (
        file_name,
        skills,
        ats_score,
        recommended_jobs
    )

    VALUES (?, ?, ?, ?)

    """, (

        file_name,
        ", ".join(skills),
        ats_score,
        ", ".join(recommended_jobs)

    ))

    conn.commit()

# ==========================
# FETCH DATA
# ==========================

def fetch_all_data():

    cursor.execute("""

    SELECT * FROM resume_analysis

    """)

    return cursor.fetchall()