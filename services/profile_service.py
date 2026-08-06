from database.lakebase import run_write
from lakebase import run_query

def get_profile(user_id):

    sql = """
    SELECT *
    FROM profiles
    WHERE user_id = %s
    LIMIT 1
    """

    result = run_query(
        sql,
        (user_id,)
    )

    if result:
        return result[0]

    return None

def create_profile(user_id, data):


    sql = """

    INSERT INTO profiles
    (
        user_id,
        first_name,
        last_name,
        location,
        target_role,
        years_experience,
        summary
    )

    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    );

    """


    run_write(
        sql,
        (
            user_id,
            data["first_name"],
            data["last_name"],
            data["location"],
            data["target_role"],
            data["years_experience"],
            data["summary"]
        )
    )