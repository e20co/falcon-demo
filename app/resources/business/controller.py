from db import Session, scoped_session
from models import Business,Address
import json

def get(business_id):
    """Returns a Business instance for the specified ID
    Args:
        business_id (int): The ID of the business
    Returns:
        models.Business
    """

    # Load the Business from the db
    return Session().query(Business).get(business_id)


def create(p):
    """Adds a business to the DB and queues it for upload

    Args:
        message (str): The message of the business
    """
    with scoped_session() as session:

        payload = json.loads(p)
        print(payload)

        # Insert the business into the DB
        business = Business()
        business.fein = payload['fein']
        date = payload['startdate']
        print(date)
        business.start_date = date['date']
        business.legal_name = payload['legalname']
        business.bus_type = payload['bustype']
        business.industry = payload['industry']

	
        address = Address()
        address.street1 = payload['street1']
        address.street2 = payload['street2']
        address.street3 = payload['street1']
        address.city = payload['city']
        address.region = payload['region']
        address.postcode = payload['postcode']
        address.timezone = payload['timezone']

        business.address = address

        session.add(address)
        session.add(business)
        session.commit()

        # Return the business ID so that the caller can track its progress
        print("id of newly commited row is "+str(business.id))
        _id = business.id

    return get(_id)
