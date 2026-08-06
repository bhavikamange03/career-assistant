from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    send_file
)

from databricks.sdk import WorkspaceClient

import io

from pypdf import PdfReader

from services.resume_service import (
    save_resume,
    get_resume,
    get_resume_by_id
)


resume_bp = Blueprint(
    "resume",
    __name__
)


# Databricks Workspace client
w = WorkspaceClient()


UPLOAD_FOLDER = (
    "/Volumes/career_copilot/"
    "documents/resumes"
)


# ==============================
# View Existing Resume PDF
# ==============================

@resume_bp.route(
    "/resume/view/<int:resume_id>"
)
def view_resume(resume_id):

    resume = get_resume_by_id(
        resume_id
    )

    if not resume:
        return "Resume not found", 404


    # Download PDF from Unity Catalog Volume
    response = w.files.download(
        resume["storage_path"]
    )


    file_bytes = response.contents.read()


    return send_file(
        io.BytesIO(file_bytes),
        mimetype="application/pdf",
        download_name=resume["file_name"]
    )



# ==============================
# Resume Upload Page
# ==============================

@resume_bp.route(
    "/resume",
    methods=["GET", "POST"]
)
def resume():

    if request.method == "POST":

        file = request.files.get(
            "resume"
        )


        if not file or file.filename == "":
            return "No file selected"



        # Read uploaded PDF
        file_content = file.read()



        # Save PDF in Databricks Volume

        volume_path = (
            f"{UPLOAD_FOLDER}/"
            f"{file.filename}"
        )


        w.files.upload(
            volume_path,
            file_content,
            overwrite=True
        )



        # Extract PDF text

        pdf_reader = PdfReader(
            io.BytesIO(file_content)
        )


        extracted_text = ""


        for page in pdf_reader.pages:

            extracted_text += (
                page.extract_text()
                or ""
            )



        # Save resume metadata in Lakebase

        save_resume(

            profile_id=4,

            file_name=file.filename,

            storage_path=volume_path,

            extracted_text=extracted_text

        )


        return redirect(
            "/resume"
        )



    # Load existing resume

    resume_data = get_resume(
        profile_id=4
    )


    return render_template(
        "resume.html",
        resume=resume_data
    )