from flask import Blueprint, render_template, request, redirect

import os

from pypdf import PdfReader

from services.resume_service import save_resume, get_resume


resume_bp = Blueprint(
    "resume",
    __name__
)


UPLOAD_FOLDER = "/Volumes/career_copilot/documents/resumes"



@resume_bp.route(
    "/resume",
    methods=["GET", "POST"]
)
def resume():


    if request.method == "POST":


        file = request.files["resume"]


        if file.filename == "":
            return "No file selected"



        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )


        # Save PDF to Unity Catalog Volume

        file.save(
            file_path
        )


        # Extract text

        reader = PdfReader(
            file_path
        )


        text = ""


        for page in reader.pages:

            text += page.extract_text() or ""



        # Save metadata in Lakebase

        save_resume(

            profile_id=3,

            file_name=file.filename,

            storage_path=file_path,

            extracted_text=text

        )


        return redirect(
            "/resume"
        )



    resume_data = get_resume(
        profile_id=3
    )


    return render_template(
        "resume.html",
        resume=resume_data
    )