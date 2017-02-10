import falcon

from resources.health_checks.view import HealthCheckView


def get_app():
    app = falcon.API()

    app.add_route("/health_checks", HealthCheckView())

    return app


application = get_app()

if __name__ == "__main__":
    application.run()
