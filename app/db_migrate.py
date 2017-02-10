#!/usr/bin/env python
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DB_URL = environ.get("DATABASE_URL", "mysql+pymysql://db_user:db_password@db/db_name")
ENGINE = create_engine(DB_URL)

# The class to use for all sessions
Session = sessionmaker(bind=ENGINE)


def init_db():
    """Initialize DB schema"""
    Base.metadata.create_all(bind=ENGINE, checkfirst=True)


if __name__ == '__main__':
    init_db()
