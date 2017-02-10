from os import environ

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DB_URL = environ.get("DATABASE_URL", "mysql+pymysql://db_user:db_password@db/db_name")
ENGINE = create_engine(DB_URL)

# The class to use for all sessions
Session = sessionmaker(bind=ENGINE)


@contextmanager
def scoped_session():
    """Provide a transactional scope around a series of operations."""
    session = Session()

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.expunge_all()
        session.close()


def init_db():
    """Initialize DB schema"""
    Base.metadata.create_all(bind=ENGINE, checkfirst=True)


def teardown_db():
    """Drop all tables in DB"""
    Base.metadata.drop_all(bind=ENGINE, checkfirst=True)
