from flask import Blueprint, render_template

from services.dashboard_service import get_dashboard_data


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
def dashboard():

    dashboard = get_dashboard_data(1)

    return render_template(
        "dashboard.html",
        dashboard=dashboard
    )