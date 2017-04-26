from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HealthCheck(Base):
    __tablename__ = 'health_checks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(255))

class Address(Base):  

    __tablename__ = 'address'  	

    id = Column(Integer, primary_key=True, autoincrement=True)
    street1 = Column(String(255))
    street2 = Column(String(255))
    street3 = Column(String(255))
    city = Column(String(255))
    region = Column(String(255))
    postcode = Column(Integer)
    timezone = Column(String(255))

class Business(Base):  

    __tablename__ = 'business'  	

    bus_type_enum = ('LLC','Sole Proprietorship','S. Corporation','L. Corporation')
    indus_type_enum = ('transportation','dining','finance','construction','retail')

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(DateTime)
    fein = Column(Integer)
    legal_name = Column(String(255))
    bus_type = Column(Enum(*bus_type_enum))
    industry  = Column(Enum(*indus_type_enum))
    address_id = Column(Integer, ForeignKey('address.id'))

    address = relationship(Address)



