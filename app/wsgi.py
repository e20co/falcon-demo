import falcon

from resources.health_checks.view import HealthCheckView


def get_app():
    app = falcon.API()

    app.add_route("/health_checks", HealthCheckView())  # POST
    app.add_route("/health_checks/{health_check_id}", HealthCheckView())  # GET .../id

    return app


application = get_app()

if __name__ == "__main__":
    application.run()
