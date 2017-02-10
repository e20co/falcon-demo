from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HealthCheck(Base):
    __tablename__ = 'health_checks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(255))
