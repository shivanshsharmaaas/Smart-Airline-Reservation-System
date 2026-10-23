# from fastapi import APIRouter
# from fastapi import Depends

# from sqlalchemy.orm import Session

# from app.database.connection import get_db

# from app.schemas.booking_schema import BookingCreate

# from app.core.security import get_current_user

# # from app.services.booking_service import (
# #     book_flight,
# #     fetch_bookings
# # )


# from app.services.booking_service import (
#     book_flight,
#     fetch_bookings,
#     cancel_booking,
#     fetch_my_bookings
# )




# router = APIRouter(
#     prefix="/bookings",
#     tags=["Bookings"]
# )


# # @router.post("/")
# # def create_booking_api(
# #     request: BookingCreate,
# #     db: Session = Depends(get_db)
# # ):

# #     booking = book_flight(
# #         db,
# #         1,
# #         request.flight_id
# #     )

# #     return booking


# @router.post("/")
# def create_booking_api(
#     request: BookingCreate,
#     db: Session = Depends(get_db)
# ):

#     booking = book_flight(
#         db,
#         1,
#         request.flight_id
#     )

#     if booking is None:
#         return {
#             "message": "Flight Not Found"
#         }

#     if booking == "FULL":
#         return {
#             "message": "Flight Full"
#         }

#     return booking





# @router.get("/")
# def get_bookings_api(
#     db: Session = Depends(get_db)
# ):

#     return fetch_bookings(db)







# @router.delete("/{booking_id}")
# def cancel_booking_api(
#     booking_id: int,
#     db: Session = Depends(get_db)
# ):

#     cancelled = cancel_booking(
#         db,
#         booking_id
#     )

#     if not cancelled:
#         return {
#             "message": "Booking Not Found"
#         }

#     return {
#         "message": "Booking Cancelled Successfully"
#     }



# @router.get("/my-bookings")
# def my_bookings(
#     current_user = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):

#     return fetch_my_bookings(
#         db,
#         1
#     )








# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from app.database.connection import get_db

# from app.schemas.booking_schema import BookingCreate

# from app.core.security import get_current_user

# from app.services.booking_service import (
#     book_flight,
#     fetch_bookings,
#     cancel_booking,
#     fetch_my_bookings
# )

# router = APIRouter(
#     prefix="/bookings",
#     tags=["Bookings"]
# )


# @router.post("/")
# def create_booking_api(
#     request: BookingCreate,
#     db: Session = Depends(get_db)
# ):

#     booking = book_flight(
#         db,
#         1,
#         request.flight_id
#     )

#     if booking is None:
#         return {
#             "message": "Flight Not Found"
#         }

#     # if booking == "FULL":
#     #     return {
#     #         "message": "Flight Full"
#     #     }

#     return booking


# @router.get("/")
# def get_bookings_api(
#     db: Session = Depends(get_db)
# ):

#     return fetch_bookings(db)


# @router.get("/my-bookings")
# def my_bookings(
#     current_user=Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):

#     return fetch_my_bookings(
#         db,
#         1
#     )


# @router.delete("/{booking_id}")
# def cancel_booking_api(
#     booking_id: int,
#     db: Session = Depends(get_db)
# ):

#     result = cancel_booking(
#     db,
#     booking_id
# )

# if not result:
#     return {
#         "message": "Booking Not Found"
#     }

# return result




from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.booking_schema import BookingCreate

from app.core.security import get_current_user

from app.services.booking_service import (
    book_flight,
    fetch_bookings,
    cancel_booking,
    fetch_my_bookings
)

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/")
def create_booking_api(
    request: BookingCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    booking = book_flight(
        db,
        current_user["sub"],
        request.flight_id
    )

    if booking is None:
        return {
            "message": "Flight Not Found"
        }

    return booking


@router.get("/")
def get_bookings_api(
    db: Session = Depends(get_db)
):

    return fetch_bookings(db)


@router.get("/my-bookings")
def my_bookings(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return fetch_my_bookings(
        db,
        1
    )


@router.delete("/{booking_id}")
def cancel_booking_api(
    booking_id: int,
    db: Session = Depends(get_db)
):

    result = cancel_booking(
        db,
        booking_id
    )

    if not result:
        return {
            "message": "Booking Not Found"
        }

    return result




    