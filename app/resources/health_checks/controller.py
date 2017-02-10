# from db import Session
from models import HealthCheck


def get(health_check_id):
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
