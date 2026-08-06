from flask import Blueprint, render_template, request, redirect

from databricks.sdk import WorkspaceClient

import io

from pypdf import PdfReader

from services.resume_service import (
    save_resume,
    get_resume
)


resume_bp = Blueprint(
    "resume",
    __name__
)


w = WorkspaceClient()


UPLOAD_FOLDER = (
    "/Volumes/career_copilot/"
    "documents/resumes"
)


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



        # Read uploaded PDF into memory

        file_content = file.read()



        # Unity Catalog Volume path

        volume_path = (
            f"{UPLOAD_FOLDER}/"
            f"{file.filename}"
        )



        # Upload PDF to Databricks Volume

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



        # Save metadata in Lakebase

        save_resume(

            profile_id=4,

            file_name=file.filename,

            storage_path=volume_path,

            extracted_text=extracted_text

        )


        return redirect(
            "/resume"
        )



    resume_data = get_resume(
        profile_id=4
    )


    return render_template(
        "resume.html",
        resume=resume_data
    )