from database.lakebase import run_query, run_write



def get_preferences(user_id):

    sql = """

    SELECT *
    FROM preferences
    WHERE user_id = %s;

    """

    return run_query(
        sql,
        (user_id,)
    )




def create_or_update_preferences(
        user_id,
        data
):

    existing = get_preferences(
        user_id
    )


    if existing:

        sql = """

        UPDATE preferences

        SET

        preferred_location = %s,
        remote_preference = %s,
        target_salary = %s,
        job_type = %s,
        sponsorship_required = %s,
        updated_at = CURRENT_TIMESTAMP

        WHERE user_id = %s;

        """


        return run_write(
            sql,
            (
                data["preferred_location"],
                data["remote_preference"],
                data["target_salary"],
                data["job_type"],
                data["sponsorship_required"],
                user_id
            )
        )


    else:

        sql = """

        INSERT INTO preferences
        (
            user_id,
            preferred_location,
            remote_preference,
            target_salary,
            job_type,
            sponsorship_required
        )

        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        );

        """


        return run_write(
            sql,
            (
                user_id,
                data["preferred_location"],
                data["remote_preference"],
                data["target_salary"],
                data["job_type"],
                data["sponsorship_required"]
            )
        )