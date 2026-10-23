# from fastapi import APIRouter
# from fastapi import Depends

# from sqlalchemy.orm import Session

# from app.database.connection import get_db

# from app.models.booking import Booking
# from app.models.flight import Flight

# router = APIRouter(
#     prefix="/dashboard",
#     tags=["Dashboard"]
# )


# @router.get("/revenue")
# def get_revenue(
#     db: Session = Depends(get_db)
# ):

#     bookings = db.query(Booking).all()

#     total_bookings = len(bookings)

#     total_revenue = 0

#     for booking in bookings:

#         flight = (
#             db.query(Flight)
#             .filter(
#                 Flight.id == booking.flight_id
#             )
#             .first()
#         )

#         if flight:
#             total_revenue += flight.price

#     return {
#         "total_bookings": total_bookings,
#         "total_revenue": total_revenue
#     }






from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.user import User
from app.models.flight import Flight
from app.models.booking import Booking
from app.models.waitlist import Waitlist


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/revenue")
def get_revenue(
    db: Session = Depends(get_db)
):

    bookings = db.query(Booking).all()

    total_bookings = len(bookings)

    total_revenue = 0

    for booking in bookings:

        flight = (
            db.query(Flight)
            .filter(
                Flight.id == booking.flight_id
            )
            .first()
        )

        if flight:
            total_revenue += flight.price

    return {
        "total_bookings": total_bookings,
        "total_revenue": total_revenue
    }


@router.get("/analytics")
def analytics(
    db: Session = Depends(get_db)
):

    total_users = db.query(User).count()

    total_flights = db.query(Flight).count()

    total_bookings = db.query(Booking).count()

    total_waitlist = db.query(Waitlist).count()

    bookings = db.query(Booking).all()

    total_revenue = 0

    for booking in bookings:

        flight = (
            db.query(Flight)
            .filter(
                Flight.id == booking.flight_id
            )
            .first()
        )

        if flight:
            total_revenue += flight.price

    return {
        "total_users": total_users,
        "total_flights": total_flights,
        "total_bookings": total_bookings,
        "total_waitlist": total_waitlist,
        "total_revenue": total_revenue
    }





