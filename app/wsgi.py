import falcon

from resources.health_checks.view import HealthCheckView
from resources.business.view import BusinessView


def get_app():
    app = falcon.API()

    app.add_route("/health_checks", BusinessView())  # POST
    app.add_route("/health_checks/{health_check_id}", HealthCheckView())  # GET .../id

    app.add_route("/business", BusinessView())  # POST
    app.add_route("/business/{business_id}", BusinessView())  # GET .../id

    return app


application = get_app()

if __name__ == "__main__":
    application.run()
