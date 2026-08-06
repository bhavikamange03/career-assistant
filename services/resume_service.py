from database.lakebase import run_query, run_write



def save_resume(
    profile_id,
    file_name,
    storage_path,
    extracted_text
):

    sql = """

    INSERT INTO resumes
    (
        profile_id,
        file_name,
        storage_path,
        extracted_text
    )

    VALUES
    (
        %s,
        %s,
        %s,
        %s
    );

    """


    return run_write(
        sql,
        (
            profile_id,
            file_name,
            storage_path,
            extracted_text
        )
    )




def get_resume(profile_id):

    sql = """

    SELECT *
    FROM resumes
    WHERE profile_id = %s
    ORDER BY created_at DESC
    LIMIT 1;

    """


    return run_query(
        sql,
        (
            profile_id,
        )
    )