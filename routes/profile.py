from flask import Blueprint, render_template, request

from services.profile_service import create_profile


profile_bp = Blueprint(
    "profile",
    __name__
)



@profile_bp.route(
    "/profile",
    methods=["GET","POST"]
)
def profile():


    if request.method == "POST":


        data = {

            "first_name": request.form["first_name"],

            "last_name": request.form["last_name"],

            "location": request.form["location"],

            "target_role": request.form["target_role"],

            "years_experience": request.form["years_experience"],

            "summary": request.form["summary"]

        }


        create_profile(
            user_id=1,
            data=data
        )


        return "Profile saved successfully"



    return render_template(
        "profile.html"
    )