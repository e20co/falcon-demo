# from db import Session
from models import HealthCheck


def get_health_check(health_check_id):
    """Returns a HealthCheck instance for the specified ID
    Args:
        health_check_id (int): The ID of the health_check
    Returns:
        models.HealthCheck
    """

    # Typically, we would load the HealthCheck from the db...
    # return Session().query(HealthCheck).get(health_check_id)

    # ...but for now, we'll just return a new instance
    fake_model = HealthCheck()
    fake_model.status = 200
    fake_model.message = "I am healthy. If you are reading this, it means you're connected!"
    return fake_model


def get_metadata(health_check):
    """Returns metadata for the specified health_check
    Args:
        health_check (models.HealthCheck): A HealthCheck instance
    Returns:
        dict
    """

    data = {}

    data["status"] = health_check.status
    data["message"] = health_check.message

    return data
