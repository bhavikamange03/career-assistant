from flask import Blueprint, render_template, request, redirect

from services.profile_service import create_profile

from services.skill_service import (
    get_skills,
    create_skill
)

from services.preference_service import (
    get_preferences,
    create_or_update_preferences
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
        profile_id=4
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
        profile_id=4,
        skill_name=skill_name,
        skill_level=skill_level
    )


    return redirect(
        "/profile"
    )

@profile_bp.route(
    "/preferences",
    methods=["GET","POST"]
)
def preferences():
    if request.method == "POST":


        data = {


            "preferred_location":
            request.form.get(
                "preferred_location"
            ),


            "remote_preference":
            request.form.get(
                "remote_preference"
            ),


            "target_salary":
            int(request.form.get("target_salary"))
            if request.form.get("target_salary")
            else None,


            "job_type":
            request.form.get(
                "job_type"
            ),


            "sponsorship_required":
            request.form.get(
                "sponsorship_required"
            ) == "on"

        }


        create_or_update_preferences(
            user_id=1,
            data=data
        )


        return redirect(
            "/preferences"
        )


    preferences = get_preferences(
        user_id=1
    )


    return render_template(
        "preferences.html",
        preferences=preferences
    )