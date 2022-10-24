from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, CHAR
from sqlalchemy.orm import relationship
from db import Base


class Years(Base):
    __tablename__ = "years"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    year = Column(Integer, unique=True, nullable=False)

    temps = relationship("Temperatures", backref='years')
    months_avg = relationship("Monthly_avg", backref='years')


class Months(Base):
    __tablename__ = "months"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    month = Column(CHAR(length=24), unique=True, nullable=False)

    temps = relationship("Temperatures", backref='months')
    months_avg = relationship("Monthly_avg", backref='months')


class Longitude(Base):
    __tablename__ = 'longitude'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    long = Column(Integer, unique=True, nullable=False)

    points = relationship("Points", backref='longitude')


class Latitude(Base):
    __tablename__ = 'latitude'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    lat = Column(Integer, unique=True, nullable=False)

    points = relationship("Points", backref='latitude')


class States(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(CHAR(length=24), unique=True, nullable=False)
    type = Column(CHAR(length=24), nullable=False)

    polygons = relationship("Polygons", backref='states')
    months_avg = relationship("Monthly_avg", backref='states')

class Polygons(Base):
    __tablename__ = 'polygons'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    array = Column(String, nullable=False, unique=True)

    points = relationship("Points", backref='polygons')


class Points(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    polygon_id = Column(Integer, ForeignKey("polygons.id"))
    long_id = Column(Integer, ForeignKey("longitude.id"), nullable=False)
    lat_id = Column(Integer, ForeignKey("latitude.id"), nullable=False)

    temps = relationship("Temperatures", backref='points')


class Temperatures(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    year_id = Column(Integer, ForeignKey("years.id"), nullable=False)
    month_id = Column(Integer,  ForeignKey("months.id"), nullable=False)
    # long_id = Column(Integer, ForeignKey("longitude.id"), nullable=False)
    # lat_id = Column(Integer, ForeignKey("latitude.id"), nullable=False)
    point_id = Column(Integer, ForeignKey("points.id"), nullable=False)
    temp = Column(Integer, nullable=False)


class Monthly_avg(Base):
    __tablename__ = 'monthly_avg'
    id = Column(Integer, primary_key=True, autoincrement="auto", nullable=False)
    year_id = Column(Integer, ForeignKey("years.id"), nullable=False)
    month_id = Column(Integer,  ForeignKey("months.id"), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    temp = Column(Integer)