from database.lakebase import run_query, run_write



def get_skills(profile_id):

    sql = """
    SELECT *
    FROM skills
    WHERE profile_id = %s;
    """

    return run_query(
        sql,
        (profile_id,)
    )




def create_skill(profile_id, skill_name, skill_level):

    sql = """

    INSERT INTO skills
    (
        profile_id,
        skill_name,
        skill_level
    )

    VALUES
    (
        %s,
        %s,
        %s
    );

    """

    return run_write(
        sql,
        (
            profile_id,
            skill_name,
            skill_level
        )
    )