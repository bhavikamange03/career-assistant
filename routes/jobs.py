from flask import Blueprint, render_template

from services.job_service import (
    fetch_remote_jobs,
    save_jobs_to_db,
    get_jobs
)


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