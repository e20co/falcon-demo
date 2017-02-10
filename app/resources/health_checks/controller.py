from db import Session, scoped_session
from models import HealthCheck


def get(health_check_id):
    """Returns a HealthCheck instance for the specified ID
    Args:
        health_check_id (int): The ID of the health_check
    Returns:
        models.HealthCheck
    """

    # Load the HealthCheck from the db
    return Session().query(HealthCheck).get(health_check_id)


def create(message):
    """Adds a health_check to the DB and queues it for upload

    Args:
        message (str): The message of the health_check
    """
    with scoped_session() as session:
        # Insert the health_check into the DB
        health_check = HealthCheck()
        health_check.message = message

        session.add(health_check)
        session.commit()

        # Return the health_check ID so that the caller can track its progress
        _id = health_check.id

    return get(_id)
