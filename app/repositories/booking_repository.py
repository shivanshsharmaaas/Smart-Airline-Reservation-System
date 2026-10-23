# from sqlalchemy.orm import Session

# from app.models.booking import Booking


# def create_booking(
#     db: Session,
#     booking: Booking
# ):

#     db.add(booking)

#     db.commit()

#     db.refresh(booking)

#     return booking


# def get_all_bookings(
#     db: Session
# ):

#     return db.query(Booking).all()



from sqlalchemy.orm import Session

from app.models.booking import Booking


def create_booking(
    db: Session,
    booking: Booking
):

    db.add(booking)

    db.commit()

    db.refresh(booking)

    return booking


def get_all_bookings(
    db: Session
):

    return db.query(Booking).all()


def get_booking_by_id(
    db: Session,
    booking_id: int
):

    return (
        db.query(Booking)
        .filter(Booking.id == booking_id)
        .first()
    )


def delete_booking(
    db: Session,
    booking
):

    db.delete(booking)

    db.commit()


def get_bookings_by_user_id(
    db: Session,
    user_id: int
):

    return (
        db.query(Booking)
        .filter(
            Booking.user_id == user_id
        )
        .all()
    )



    






