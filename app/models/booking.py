# from sqlalchemy import Column
# from sqlalchemy import Integer
# from sqlalchemy import ForeignKey

# from app.database.base import Base


# class Booking(Base):

#     __tablename__ = "bookings"

#     id = Column(
#         Integer,
#         primary_key=True,
#         index=True
#     )

#     user_id = Column(
#         Integer,
#         ForeignKey("users.id")
#     )

#     flight_id = Column(
#         Integer,
#         ForeignKey("flights.id")
#     )




from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.base import Base


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    flight_id = Column(
        Integer,
        ForeignKey("flights.id")
    )

    seat_no = Column(String(10))



    