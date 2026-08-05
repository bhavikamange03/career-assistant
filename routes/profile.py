from flask import Blueprint, render_template, request, redirect

from services.profile_service import create_profile

from services.skill_service import (
    get_skills,
    create_skill
)


profile_bp = Blueprint(
    "profile",
    __name__
)



@profile_bp.route(
    "/profile",
    methods=["GET", "POST"]
)
def profile():

    if request.method == "POST":

        data = {

            "first_name": request.form.get("first_name"),

            "last_name": request.form.get("last_name"),

            "location": request.form.get("location"),

            "target_role": request.form.get("target_role"),

            "years_experience": request.form.get("years_experience"),

            "summary": request.form.get("summary")

        }


        create_profile(
            user_id=1,
            data=data
        )


        return redirect("/profile")


    skills = get_skills(
        profile_id=1
    )


    return render_template(
        "profile.html",
        skills=skills
    )



@profile_bp.route(
    "/add-skill",
    methods=["POST"]
)
def add_skill():

    skill_name = request.form.get(
        "skill_name"
    )


    skill_level = request.form.get(
        "skill_level"
    )


    create_skill(
        profile_id=1,
        skill_name=skill_name,
        skill_level=skill_level
    )


    return redirect(
        "/profile"
    )