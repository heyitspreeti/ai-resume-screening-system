from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    filename,
    skills,
    ats_score,
    recommended_jobs
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "AI Resume Analysis Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # =========================
    # ATS SCORE
    # =========================

    ats = Paragraph(
        f"<b>ATS Score:</b> {ats_score}%",
        styles['BodyText']
    )

    elements.append(ats)

    elements.append(Spacer(1, 15))

    # =========================
    # SKILLS
    # =========================

    skills_title = Paragraph(
        "<b>Detected Skills:</b>",
        styles['Heading2']
    )

    elements.append(skills_title)

    for skill in skills:
        skill_para = Paragraph(
            f"• {skill}",
            styles['BodyText']
        )

        elements.append(skill_para)

    elements.append(Spacer(1, 15))

    # =========================
    # JOBS
    # =========================

    jobs_title = Paragraph(
        "<b>Recommended Jobs:</b>",
        styles['Heading2']
    )

    elements.append(jobs_title)

    for job in recommended_jobs:
        job_para = Paragraph(
            f"• {job}",
            styles['BodyText']
        )

        elements.append(job_para)

    doc.build(elements)