from database.lakebase import run_query


def get_dashboard_data(user_id):

    profile = run_query(
        """
        SELECT *
        FROM profiles
        WHERE user_id = %s;
        """,
        (user_id,)
    )


    resume = run_query(
        """
        SELECT *
        FROM resumes
        WHERE profile_id IN (
            SELECT id
            FROM profiles
            WHERE user_id = %s
        );
        """,
        (user_id,)
    )


    saved_jobs = run_query(
        """
        SELECT COUNT(*) as count
        FROM saved_jobs
        WHERE user_id = %s;
        """,
        (user_id,)
    )


    applications = run_query(
        """
        SELECT COUNT(*) as count
        FROM applications
        WHERE user_id = %s;
        """,
        (user_id,)
    )


    return {

        "profile_completed": len(profile) > 0,

        "resume_uploaded": len(resume) > 0,

        "saved_jobs": saved_jobs[0]["count"],

        "applications": applications[0]["count"]

    }