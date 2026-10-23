# from sqlalchemy.orm import Session

# from app.models.flight import Flight


# def create_flight(
#     db: Session,
#     flight: Flight
# ):

#     db.add(flight)

#     db.commit()

#     db.refresh(flight)

#     return flight


# def get_all_flights(
#     db: Session
# ):

#     return db.query(Flight).all()







# def get_flight_by_id(
#     db: Session,
#     flight_id: int
# ):
#     return (
#         db.query(Flight)
#         .filter(Flight.id == flight_id)
#         .first()
#     )



# def delete_flight(
#     db: Session,
#     flight
# ):
#     db.delete(flight)

#     db.commit()




from sqlalchemy.orm import Session

from app.models.flight import Flight


def create_flight(
    db: Session,
    flight: Flight
):

    db.add(flight)

    db.commit()

    db.refresh(flight)

    return flight


def get_all_flights(
    db: Session
):

    return db.query(Flight).all()


def get_flight_by_id(
    db: Session,
    flight_id: int
):

    return (
        db.query(Flight)
        .filter(Flight.id == flight_id)
        .first()
    )


def delete_flight(
    db: Session,
    flight
):

    db.delete(flight)
    db.commit()




def update_flight(db, flight):

    db.commit()

    db.refresh(flight)

    return flight





def search_flights(
    db: Session,
    source: str,
    destination: str
):

    return (
        db.query(Flight)
        .filter(
            Flight.source == source,
            Flight.destination == destination
        )
        .all()
    )







def update_flight_details(
    db: Session,
    flight,
    request
):

    flight.flight_number = request.flight_number
    flight.source = request.source
    flight.destination = request.destination
    flight.departure_time = request.departure_time
    flight.arrival_time = request.arrival_time
    flight.price = request.price
    flight.available_seats = request.available_seats

    flight.status = request.status

    db.commit()

    db.refresh(flight)

    return flight




