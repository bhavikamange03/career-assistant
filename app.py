from flask import Flask, render_template

from routes.profile import profile_bp

from routes.resume import resume_bp

from routes.jobs import jobs_bp

from services.dashboard_service import get_dashboard_data

app = Flask(__name__)
app.register_blueprint(profile_bp)
app.register_blueprint(resume_bp)
app.regsiter_blueprint(jobs_bp)
@app.route("/")
def home():

    user_id = 1

    dashboard = get_dashboard_data(user_id)


    return render_template(
        "dashboard.html",
        dashboard=dashboard
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)