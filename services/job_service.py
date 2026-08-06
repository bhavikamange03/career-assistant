import requests

from lakebase import run_query, run_write


def fetch_remote_jobs():

    response = requests.get(
        "https://remoteok.com/api",
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    data = response.json()

    jobs = []

    for item in data[1:20]:

        jobs.append({
            "external_id": str(item.get("id")),
            "title": item.get("position"),
            "company": item.get("company"),
            "location": item.get("location"),
            "url": item.get("url"),
            "description": item.get("description")
        })

    return jobs



def save_jobs_to_db(jobs):

    for job in jobs:

        sql = """
        INSERT INTO job_postings
        (
            external_id,
            title,
            company,
            location,
            url,
            description
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s
        )
        """

        run_write(
            sql,
            (
                job["external_id"],
                job["title"],
                job["company"],
                job["location"],
                job["url"],
                job["description"]
            )
        )



def get_jobs():

    sql = """
    SELECT *
    FROM job_postings
    ORDER BY created_at DESC
    LIMIT 50
    """

    return run_query(sql)