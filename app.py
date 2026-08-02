from flask import Flask, render_template, request
from google import genai
from config import GEMINI_API_KEY

app = Flask(__name__)

client = genai.Client(api_key=GEMINI_API_KEY)


@app.route("/", methods=["GET", "POST"])
def home():

    # -----------------------------
    # Personal Information
    # -----------------------------
    full_name = ""
    email = ""
    contact_info = ""

    # -----------------------------
    # Education
    # -----------------------------
    school = ""
    degree = ""
    field = ""

    # -----------------------------
    # Experience
    # -----------------------------
    company = ""
    job_title = ""
    responsibilities = ""

    # -----------------------------
    # Projects
    # -----------------------------
    project_name = ""
    technologies = ""
    project_description = ""
    github_link = ""

    # -----------------------------
    # Skills
    # -----------------------------
    skills_learnt = ""

    # -----------------------------
    # Languages
    # -----------------------------
    languages = ""

    # -----------------------------
    # Certifications
    # -----------------------------
    certificate = ""
    certificate_description = ""
    certificate_date = ""

    # -----------------------------
    # Links
    # -----------------------------
    linkedin = ""
    portfolio = ""

    # -----------------------------
    # Career Objective
    # -----------------------------
    career_objective = ""

    # -----------------------------
    # AI Resume
    # -----------------------------
    resume = ""

    if request.method == "POST":

        # Personal Information
        full_name = request.form.get("full-name", "")
        email = request.form.get("email", "")
        contact_info = request.form.get("contact-info", "")

        # Education
        school = request.form.get("School", "")
        degree = request.form.get("Degree", "")
        field = request.form.get("field", "")

        # Experience
        company = request.form.get("Company", "")
        job_title = request.form.get("jobtitle", "")
        responsibilities = request.form.get("Responsibilities", "")

        # Projects
        project_name = request.form.get("projectname", "")
        technologies = request.form.get("tech", "")
        project_description = request.form.get("desc", "")
        github_link = request.form.get("github-link", "")

        # Skills
        skills_learnt = request.form.get("Skills-learnt", "")

        # Languages
        languages = request.form.get("lang", "")

        # Certifications
        certificate = request.form.get("cert", "")
        certificate_description = request.form.get("descert", "")
        certificate_date = request.form.get("certdate", "")

        # Links
        linkedin = request.form.get("linkedinlink", "")
        portfolio = request.form.get("Projectlink", "")

        # Career Objective
        career_objective = request.form.get("Careerobj", "")

        # -----------------------------
        # Gemini Prompt
        # -----------------------------

        prompt = f"""
You are an expert resume writer and ATS optimization specialist.

Using ONLY the information provided below:

- Do NOT invent any information.
- Improve grammar and wording.
- Use powerful action verbs.
- Make the resume modern and ATS-friendly.
- Omit empty sections.
- Return ONLY clean HTML.
- Do NOT include html, head or body tags.
- Use only:
<h1>
<h2>
<p>
<ul>
<li>
<strong>
<hr>

Candidate Information

Name:
{full_name}

Email:
{email}

Contact:
{contact_info}

Career Objective:
{career_objective}

Education

School:
{school}

Degree:
{degree}

Field:
{field}

Experience

Company:
{company}

Job Title:
{job_title}

Responsibilities:
{responsibilities}

Projects

Project Name:
{project_name}

Technologies:
{technologies}

Description:
{project_description}

Github:
{github_link}

Skills:
{skills_learnt}

Languages:
{languages}

Certifications

Certificate:
{certificate}

Description:
{certificate_description}

Issued:
{certificate_date}

Links

LinkedIn:
{linkedin}

Portfolio:
{portfolio}
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            resume = response.text

        except Exception as e:

            resume = f"<h2>Error</h2><p>{e}</p>"

    return render_template(
        "index.html",

        # Personal Information
        full_name=full_name,
        email=email,
        contact_info=contact_info,

        # Education
        school=school,
        degree=degree,
        field=field,

        # Experience
        company=company,
        job_title=job_title,
        responsibilities=responsibilities,

        # Projects
        project_name=project_name,
        technologies=technologies,
        project_description=project_description,
        github_link=github_link,

        # Skills
        skills_learnt=skills_learnt,

        # Languages
        languages=languages,

        # Certifications
        certificate=certificate,
        certificate_description=certificate_description,
        certificate_date=certificate_date,

        # Links
        linkedin=linkedin,
        portfolio=portfolio,

        # Career Objective
        career_objective=career_objective,

        # AI Resume
        resume=resume
    )


if __name__ == "__main__":
    app.run(debug=True)