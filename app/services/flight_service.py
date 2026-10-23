# from app.models.flight import Flight

# from app.repositories.flight_repository import (
#     create_flight,
#     get_all_flights
# )


# def add_flight(
#     db,
#     request
# ):

#     flight = Flight(

#         flight_number=request.flight_number,

#         source=request.source,

#         destination=request.destination,

#         departure_time=request.departure_time,

#         arrival_time=request.arrival_time,

#         price=request.price,

#         available_seats=request.available_seats
#     )

#     return create_flight(
#         db,
#         flight
#     )


# def fetch_flights(
#     db
# ):
#     return get_all_flights(db)



# from app.repositories.flight_repository import (
#     get_flight_by_id,
#     delete_flight
# )


# def fetch_flight_by_id(
#     db,
#     flight_id
# ):
#     return get_flight_by_id(
#         db,
#         flight_id
#     )




# def remove_flight(
#     db,
#     flight_id
# ):

#     flight = get_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return False

#     delete_flight(
#         db,
#         flight
#     )

#     return True




from app.models.flight import Flight

from app.repositories.flight_repository import (
    create_flight,
    get_all_flights,
    get_flight_by_id,
    delete_flight
)


def add_flight(
    db,
    request
):

    # flight = Flight(
    #     flight_number=request.flight_number,
    #     source=request.source,
    #     destination=request.destination,
    #     departure_time=request.departure_time,
    #     arrival_time=request.arrival_time,
    #     price=request.price,
    #     available_seats=request.available_seats
    # )
    flight = Flight(
    flight_number=request.flight_number,
    source=request.source,
    destination=request.destination,
    departure_time=request.departure_time,
    arrival_time=request.arrival_time,
    price=request.price,
    available_seats=request.available_seats,
    status=request.status
)

    return create_flight(
        db,
        flight
    )


def fetch_flights(db):
    return get_all_flights(db)


def fetch_flight_by_id(
    db,
    flight_id
):
    return get_flight_by_id(
        db,
        flight_id
    )


def remove_flight(
    db,
    flight_id
):

    flight = get_flight_by_id(
        db,
        flight_id
    )

    if not flight:
        return False

    delete_flight(
        db,
        flight
    )

    return True


from app.repositories.flight_repository import (
    create_flight,
    get_all_flights,
    get_flight_by_id,
    delete_flight,
    search_flights,
    update_flight_details
)




def search_flight_service(
    db,
    source,
    destination
):

    return search_flights(
        db,
        source,
        destination
    )






def update_flight_service(
    db,
    flight_id,
    request
):

    flight = get_flight_by_id(
        db,
        flight_id
    )

    if not flight:
        return None

    return update_flight_details(
        db,
        flight,
        request
    )






