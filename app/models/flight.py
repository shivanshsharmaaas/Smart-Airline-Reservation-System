from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database.base import Base


class Flight(Base):

    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)

    flight_number = Column(String(50))

    source = Column(String(100))

    destination = Column(String(100))

    departure_time = Column(String(50))

    arrival_time = Column(String(50))

    price = Column(Float)

    available_seats = Column(Integer)


    status = Column(
    String(50),
    default="ON_TIME"
)





