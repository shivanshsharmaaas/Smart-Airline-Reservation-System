from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database.base import Base


class Waitlist(Base):

    __tablename__ = "waitlist"

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

    waitlist_no = Column(Integer)



