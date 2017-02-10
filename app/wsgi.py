import falcon

from resources.health_check import HealthCheck


def get_app():
    app = falcon.API()

    app.add_route("/health_checks", HealthCheck())

    return app


application = get_app()

if __name__ == "__main__":
    application.run()
