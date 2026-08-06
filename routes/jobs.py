from flask import Blueprint, render_template, request, redirect

from services.job_service import (
    fetch_remote_jobs,
    save_jobs_to_db,
    get_jobs
)

from database.lakebase import run_write


jobs_bp = Blueprint(
    "jobs",
    __name__
)


@jobs_bp.route("/jobs")
def jobs():

    jobs = fetch_remote_jobs()

    save_jobs_to_db(jobs)

    saved_jobs = get_jobs()

    return render_template(
        "jobs.html",
        jobs=saved_jobs
    )


@jobs_bp.route("/save-job", methods=["POST"])
def save_job():

    job_id = request.form["job_id"]

    sql = """
    INSERT INTO saved_jobs
    (
        user_id,
        job_id
    )
    VALUES
    (
        %s,
        %s
    )
    """

    run_write(
        sql,
        (
            1,       # temporary user_id for Day 1 MVP
            job_id
        )
    )

    return redirect("/jobs")