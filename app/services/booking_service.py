# from app.models.booking import Booking

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings
# )


# def book_flight(
#     db,
#     user_id,
#     flight_id
# ):

#     booking = Booking(
#         user_id=user_id,
#         flight_id=flight_id
#     )

#     return create_booking(
#         db,
#         booking
#     )


# def fetch_bookings(
#     db
# ):

#     return get_all_bookings(db)





# from app.models.booking import Booking

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings
# )

# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     update_flight
# )


# def book_flight(
#     db,
#     user_id,
#     flight_id
# ):

#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return None

#     if flight.available_seats <= 0:
#         return "FULL"

#     flight.available_seats -= 1

#     update_flight(
#         db,
#         flight
#     )

#     booking = Booking(
#         user_id=user_id,
#         flight_id=flight_id
#     )

#     return create_booking(
#         db,
#         booking
#     )


# def fetch_bookings(db):

#     return get_all_bookings(db)





# from app.models.booking import Booking

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings,
#     get_booking_by_id,
#     delete_booking
# )

# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     update_flight
# )





# def generate_seat_number(
#     total_bookings
# ):

#     return f"A{total_bookings + 1}"




# def book_flight(
#     db,
#     user_id,
#     flight_id
# ):

#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return None

#     if flight.available_seats <= 0:
#         return "FULL"

#     flight.available_seats -= 1

#     update_flight(
#         db,
#         flight
#     )



#     all_bookings = get_all_bookings(db)

# seat_no = generate_seat_number(
#     len(all_bookings)
# )

#     # booking = Booking(
#     #     user_id=user_id,
#     #     flight_id=flight_id
#     # )

#     booking = Booking(
#     user_id=user_id,
#     flight_id=flight_id,
#     seat_no=seat_no
# )

#     return create_booking(
#         db,
#         booking
#     )


# def fetch_bookings(
#     db
# ):

#     return get_all_bookings(db)


# def cancel_booking(
#     db,
#     booking_id
# ):

#     booking = get_booking_by_id(
#         db,
#         booking_id
#     )

#     if not booking:
#         return False

#     flight = get_flight_by_id(
#         db,
#         booking.flight_id
#     )

#     if flight:

#         flight.available_seats += 1

#         update_flight(
#             db,
#             flight
#         )

#     delete_booking(
#         db,
#         booking
#     )

#     return True








# from app.models.booking import Booking

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings,
#     get_booking_by_id,
#     delete_booking,
#     get_bookings_by_user_id
# )

# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     update_flight
# )


# def generate_seat_number(total_bookings):

#     return f"A{total_bookings + 1}"


# def book_flight(
#     db,
#     user_id,
#     flight_id
# ):

#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return None

#     if flight.available_seats <= 0:
#         return "FULL"

#     flight.available_seats -= 1

#     update_flight(
#         db,
#         flight
#     )

#     all_bookings = get_all_bookings(db)

#     seat_no = generate_seat_number(
#         len(all_bookings)
#     )

#     booking = Booking(
#         user_id=user_id,
#         flight_id=flight_id,
#         seat_no=seat_no
#     )

#     return create_booking(
#         db,
#         booking
#     )


# def fetch_bookings(
#     db
# ):

#     return get_all_bookings(db)


# def cancel_booking(
#     db,
#     booking_id
# ):

#     booking = get_booking_by_id(
#         db,
#         booking_id
#     )

#     if not booking:
#         return False

#     flight = get_flight_by_id(
#         db,
#         booking.flight_id
#     )

#     if flight:

#         flight.available_seats += 1

#         update_flight(
#             db,
#             flight
#         )

#     delete_booking(
#         db,
#         booking
#     )

#     return True



# def fetch_my_bookings(
#     db,
#     user_id
# ):

#     return get_bookings_by_user_id(
#         db,
#         user_id
#     )






# from app.models.booking import Booking

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings,
#     get_booking_by_id,
#     delete_booking,
#     get_bookings_by_user_id
# )

# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     update_flight
# )

# from app.utils.qr_generator import generate_ticket_qr


# def generate_seat_number(total_bookings):

#     return f"A{total_bookings + 1}"


# def book_flight(
#     db,
#     user_id,
#     flight_id
# ):

#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return None

#     if flight.available_seats <= 0:
#         return "FULL"

#     flight.available_seats -= 1

#     update_flight(
#         db,
#         flight
#     )

#     all_bookings = get_all_bookings(db)

#     seat_no = generate_seat_number(
#         len(all_bookings)
#     )

#     booking = Booking(
#         user_id=user_id,
#         flight_id=flight_id,
#         seat_no=seat_no
#     )

#     booking = create_booking(
#         db,
#         booking
#     )

#     qr_file = generate_ticket_qr(
#         f"BOOKING-{booking.id}"
#     )

#     return {
#         "booking_id": booking.id,
#         "user_id": booking.user_id,
#         "flight_id": booking.flight_id,
#         "seat_no": booking.seat_no,
#         "qr_file": qr_file
#     }


# def fetch_bookings(
#     db
# ):

#     return get_all_bookings(db)


# def cancel_booking(
#     db,
#     booking_id
# ):

#     booking = get_booking_by_id(
#         db,
#         booking_id
#     )

#     if not booking:
#         return False

#     flight = get_flight_by_id(
#         db,
#         booking.flight_id
#     )

#     if flight:

#         flight.available_seats += 1

#         update_flight(
#             db,
#             flight
#         )

#     delete_booking(
#         db,
#         booking
#     )

#     return True


# def fetch_my_bookings(
#     db,
#     user_id
# ):

#     return get_bookings_by_user_id(
#         db,
#         user_id
#     )





# from app.models.booking import Booking
# from app.models.waitlist import Waitlist

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings,
#     get_booking_by_id,
#     delete_booking,
#     get_bookings_by_user_id
# )

# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     update_flight
# )


# from app.repositories.waitlist_repository import (
#     create_waitlist,
#     get_waitlist_count
# )



# from app.utils.qr_generator import generate_ticket_qr
# from app.utils.pdf_generator import generate_ticket_pdf


# def generate_seat_number(total_bookings):

#     return f"A{total_bookings + 1}"


# def book_flight(
#     db,
#     user_id,
#     flight_id
# ):

#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return None

#     # if flight.available_seats <= 0:
#     #     return "FULL"
#     if flight.available_seats <= 0:

#     count = get_waitlist_count(
#         db,
#         flight_id
#     )

#     waitlist = Waitlist(
#         user_id=user_id,
#         flight_id=flight_id,
#         waitlist_no=count + 1
#     )

#     create_waitlist(
#         db,
#         waitlist
#     )

#     return {
#         "message": "Added To Waitlist",
#         "waitlist_no": count + 1
#     }

#     flight.available_seats -= 1

#     update_flight(
#         db,
#         flight
#     )

#     all_bookings = get_all_bookings(db)

#     seat_no = generate_seat_number(
#         len(all_bookings)
#     )

#     booking = Booking(
#         user_id=user_id,
#         flight_id=flight_id,
#         seat_no=seat_no
#     )

#     booking = create_booking(
#         db,
#         booking
#     )

#     qr_file = generate_ticket_qr(
#         f"BOOKING-{booking.id}"
#     )

#     pdf_file = generate_ticket_pdf(
#         booking.id,
#         booking.user_id,
#         booking.flight_id,
#         booking.seat_no
#     )

#     return {
#         "booking_id": booking.id,
#         "user_id": booking.user_id,
#         "flight_id": booking.flight_id,
#         "seat_no": booking.seat_no,
#         "qr_file": qr_file,
#         "pdf_ticket": pdf_file
#     }


# def fetch_bookings(
#     db
# ):

#     return get_all_bookings(db)


# def cancel_booking(
#     db,
#     booking_id
# ):

#     booking = get_booking_by_id(
#         db,
#         booking_id
#     )

#     if not booking:
#         return False

#     flight = get_flight_by_id(
#         db,
#         booking.flight_id
#     )

#     if flight:

#         flight.available_seats += 1

#         update_flight(
#             db,
#             flight
#         )

#     delete_booking(
#         db,
#         booking
#     )

#     return True


# def fetch_my_bookings(
#     db,
#     user_id
# ):

#     return get_bookings_by_user_id(
#         db,
#         user_id
#     )





# from app.models.booking import Booking
# from app.models.waitlist import Waitlist

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings,
#     get_booking_by_id,
#     delete_booking,
#     get_bookings_by_user_id
# )

# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     update_flight
# )

# from app.repositories.waitlist_repository import (
#     create_waitlist,
#     get_waitlist_count
# )

# from app.repositories.waitlist_repository import (
#     create_waitlist,
#     get_waitlist_count,
#     get_first_waitlist,
#     delete_waitlist
# )

# from app.utils.qr_generator import generate_ticket_qr
# from app.utils.pdf_generator import generate_ticket_pdf


# def generate_seat_number(total_bookings):

#     return f"A{total_bookings + 1}"


# def book_flight(
#     db,
#     user_id,
#     flight_id
# ):

#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return None

#     if flight.available_seats <= 0:

#         count = get_waitlist_count(
#             db,
#             flight_id
#         )

#         waitlist = Waitlist(
#             user_id=user_id,
#             flight_id=flight_id,
#             waitlist_no=count + 1
#         )

#         create_waitlist(
#             db,
#             waitlist
#         )

#         return {
#             "message": "Added To Waitlist",
#             "waitlist_no": count + 1
#         }

#     flight.available_seats -= 1

#     update_flight(
#         db,
#         flight
#     )

#     all_bookings = get_all_bookings(db)

#     seat_no = generate_seat_number(
#         len(all_bookings)
#     )

#     booking = Booking(
#         user_id=user_id,
#         flight_id=flight_id,
#         seat_no=seat_no
#     )

#     booking = create_booking(
#         db,
#         booking
#     )

#     qr_file = generate_ticket_qr(
#         f"BOOKING-{booking.id}"
#     )

#     pdf_file = generate_ticket_pdf(
#         booking.id,
#         booking.user_id,
#         booking.flight_id,
#         booking.seat_no
#     )

#     return {
#         "booking_id": booking.id,
#         "user_id": booking.user_id,
#         "flight_id": booking.flight_id,
#         "seat_no": booking.seat_no,
#         "qr_file": qr_file,
#         "pdf_ticket": pdf_file
#     }


# def fetch_bookings(
#     db
# ):

#     return get_all_bookings(db)


# def cancel_booking(
#     db,
#     booking_id
# ):

#     booking = get_booking_by_id(
#         db,
#         booking_id
#     )

#     if not booking:
#         return False

#     flight = get_flight_by_id(
#         db,
#         booking.flight_id
#     )

#     if flight:

#     first_waitlist = get_first_waitlist(
#         db,
#         flight.id
#     )

#     if first_waitlist:

#         all_bookings = get_all_bookings(db)

#         seat_no = generate_seat_number(
#             len(all_bookings)
#         )

#         new_booking = Booking(
#             user_id=first_waitlist.user_id,
#             flight_id=flight.id,
#             seat_no=seat_no
#         )

#         create_booking(
#             db,
#             new_booking
#         )

#         delete_waitlist(
#             db,
#             first_waitlist
#         )

#     else:

#         flight.available_seats += 1

#         update_flight(
#             db,
#             flight
#         )

#     delete_booking(
#         db,
#         booking
#     )

#     return True


# def fetch_my_bookings(
#     db,
#     user_id
# ):

#     return get_bookings_by_user_id(
#         db,
#         user_id
#     )







# from app.models.booking import Booking
# from app.models.waitlist import Waitlist

# from app.repositories.booking_repository import (
#     create_booking,
#     get_all_bookings,
#     get_booking_by_id,
#     delete_booking,
#     get_bookings_by_user_id
# )

# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     update_flight
# )

# from app.repositories.waitlist_repository import (
#     create_waitlist,
#     get_waitlist_count,
#     get_first_waitlist,
#     delete_waitlist
# )




# from app.utils.email_service import (
#     send_ticket_email
# )


# from app.repositories.user_repository import (
#     get_user_by_email
# )




# from app.utils.qr_generator import generate_ticket_qr
# from app.utils.pdf_generator import generate_ticket_pdf
# from app.utils.email_service import send_ticket_email


# def generate_seat_number(total_bookings):

#     return f"A{total_bookings + 1}"


# def book_flight(
#     db,
#     user_email,
#     flight_id
# ):

#   user = get_user_by_email(
#     db,
#     user_email
# )

# if not user:
#     return None

# user_id = user.id



#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )


#     if not flight:
#         return None

#     if flight.available_seats <= 0:

#         count = get_waitlist_count(
#             db,
#             flight_id
#         )

#         waitlist = Waitlist(
#             user_id=user_id,
#             flight_id=flight_id,
#             waitlist_no=count + 1
#         )

#         create_waitlist(
#             db,
#             waitlist
#         )

#         return {
#             "message": "Added To Waitlist",
#             "waitlist_no": count + 1
#         }

#     flight.available_seats -= 1

#     update_flight(
#         db,
#         flight
#     )

#     all_bookings = get_all_bookings(db)

#     seat_no = generate_seat_number(
#         len(all_bookings)
#     )

#     booking = Booking(
#         user_id=user_id,
#         flight_id=flight_id,
#         seat_no=seat_no
#     )

#     booking = create_booking(
#         db,
#         booking
#     )

#     qr_file = generate_ticket_qr(
#         f"BOOKING-{booking.id}"
#     )

#     pdf_file = generate_ticket_pdf(
#         booking.id,
#         booking.user_id,
#         booking.flight_id,
#         booking.seat_no
#     )
#     send_ticket_email(
#     user.email,
#     booking.id,
#     pdf_file
#      )

#     return {
#         "booking_id": booking.id,
#         "user_id": booking.user_id,
#         "flight_id": booking.flight_id,
#         "seat_no": booking.seat_no,
#         "qr_file": qr_file,
#         "pdf_ticket": pdf_file
#     }


# def fetch_bookings(
#     db
# ):

#     return get_all_bookings(db)


# def cancel_booking(
#     db,
#     booking_id
# ):

#     booking = get_booking_by_id(
#         db,
#         booking_id
#     )

#     if not booking:
#         return False

#     flight = get_flight_by_id(
#         db,
#         booking.flight_id
#     )

#     if flight:

#         first_waitlist = get_first_waitlist(
#             db,
#             flight.id
#         )

#         if first_waitlist:

#             all_bookings = get_all_bookings(db)

#             seat_no = generate_seat_number(
#                 len(all_bookings)
#             )

#             new_booking = Booking(
#                 user_id=first_waitlist.user_id,
#                 flight_id=flight.id,
#                 seat_no=seat_no
#             )

#             create_booking(
#                 db,
#                 new_booking
#             )

#             delete_waitlist(
#                 db,
#                 first_waitlist
#             )

#         else:

#             flight.available_seats += 1

#             update_flight(
#                 db,
#                 flight
#             )

#     refund_amount = 0

#     if flight:
#         refund_amount = flight.price

#     delete_booking(
#         db,
#         booking
#     )

#     return {
#         "message": "Booking Cancelled Successfully",
#         "refund_amount": refund_amount,
#         "refund_status": "INITIATED"
#     }


# def fetch_my_bookings(
#     db,
#     user_id
# ):

#     return get_bookings_by_user_id(
#         db,
#         user_id
#     )





from app.models.booking import Booking
from app.models.waitlist import Waitlist

from app.repositories.booking_repository import (
    create_booking,
    get_all_bookings,
    get_booking_by_id,
    delete_booking,
    get_bookings_by_user_id
)

from app.repositories.flight_repository import (
    get_flight_by_id,
    update_flight
)

from app.repositories.waitlist_repository import (
    create_waitlist,
    get_waitlist_count,
    get_first_waitlist,
    delete_waitlist
)

from app.repositories.user_repository import (
    get_user_by_email
)

from app.utils.qr_generator import generate_ticket_qr
from app.utils.pdf_generator import generate_ticket_pdf
from app.utils.email_service import send_ticket_email


def generate_seat_number(total_bookings):

    return f"A{total_bookings + 1}"


def book_flight(
    db,
    user_email,
    flight_id
):

    user = get_user_by_email(
        db,
        user_email
    )

    if not user:
        return None

    user_id = user.id

    flight = get_flight_by_id(
        db,
        flight_id
    )

    if not flight:
        return None

    if flight.available_seats <= 0:

        count = get_waitlist_count(
            db,
            flight_id
        )

        waitlist = Waitlist(
            user_id=user_id,
            flight_id=flight_id,
            waitlist_no=count + 1
        )

        create_waitlist(
            db,
            waitlist
        )

        return {
            "message": "Added To Waitlist",
            "waitlist_no": count + 1
        }

    flight.available_seats -= 1

    update_flight(
        db,
        flight
    )

    all_bookings = get_all_bookings(db)

    seat_no = generate_seat_number(
        len(all_bookings)
    )

    booking = Booking(
        user_id=user_id,
        flight_id=flight_id,
        seat_no=seat_no
    )

    booking = create_booking(
        db,
        booking
    )

    qr_file = generate_ticket_qr(
        f"BOOKING-{booking.id}"
    )

    pdf_file = generate_ticket_pdf(
        booking.id,
        booking.user_id,
        booking.flight_id,
        booking.seat_no
    )

    send_ticket_email(
        user.email,
        booking.id,
        pdf_file
    )

    return {
        "booking_id": booking.id,
        "user_id": booking.user_id,
        "flight_id": booking.flight_id,
        "seat_no": booking.seat_no,
        "qr_file": qr_file,
        "pdf_ticket": pdf_file
    }


def fetch_bookings(
    db
):

    return get_all_bookings(db)


def cancel_booking(
    db,
    booking_id
):

    booking = get_booking_by_id(
        db,
        booking_id
    )

    if not booking:
        return False

    flight = get_flight_by_id(
        db,
        booking.flight_id
    )

    if flight:

        first_waitlist = get_first_waitlist(
            db,
            flight.id
        )

        if first_waitlist:

            all_bookings = get_all_bookings(db)

            seat_no = generate_seat_number(
                len(all_bookings)
            )

            new_booking = Booking(
                user_id=first_waitlist.user_id,
                flight_id=flight.id,
                seat_no=seat_no
            )

            create_booking(
                db,
                new_booking
            )

            delete_waitlist(
                db,
                first_waitlist
            )

        else:

            flight.available_seats += 1

            update_flight(
                db,
                flight
            )

    refund_amount = 0

    if flight:
        refund_amount = flight.price

    delete_booking(
        db,
        booking
    )

    return {
        "message": "Booking Cancelled Successfully",
        "refund_amount": refund_amount,
        "refund_status": "INITIATED"
    }


def fetch_my_bookings(
    db,
    user_id
):

    return get_bookings_by_user_id(
        db,
        user_id
    )


    