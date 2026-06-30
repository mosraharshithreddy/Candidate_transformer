from flask import Flask, render_template, request, send_file
import os

from src.pipeline import process_candidate

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("output", exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    resume = request.files["resume"]
    recruiter = request.files["recruiter"]
    github = request.form.get("github")

    resume_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename,
    )

    recruiter_path = os.path.join(
        UPLOAD_FOLDER,
        recruiter.filename,
    )

    resume.save(resume_path)
    recruiter.save(recruiter_path)

    try:

        candidate = process_candidate(
            resume_path=resume_path,
            recruiter_csv_path=recruiter_path,
            github_username=github,
        )

        return render_template(
            "result.html",
            candidate=candidate,
        )

    except Exception as e:

        return render_template(
            "error.html",
            message=str(e),
        )


@app.route("/download/candidate")
def download_candidate():

    return send_file(
        "output/candidate.json",
        as_attachment=True,
    )


@app.route("/download/projected")
def download_projected():

    return send_file(
        "output/projected_candidate.json",
        as_attachment=True,
    )


if __name__ == "__main__":
    app.run(debug=True)