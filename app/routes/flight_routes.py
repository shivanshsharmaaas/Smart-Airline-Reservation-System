# from fastapi import APIRouter
# from fastapi import Depends

# from sqlalchemy.orm import Session

# from app.database.connection import get_db

# from app.schemas.flight_schema import FlightCreate

# from app.services.flight_service import (
#     add_flight,
#     fetch_flights
# )


# router = APIRouter(
#     prefix="/flights",
#     tags=["Flights"]
# )


# @router.post("/")
# def create_new_flight(
#     request: FlightCreate,
#     db: Session = Depends(get_db)
# ):

#     add_flight(
#         db,
#         request
#     )

#     return {
#         "message": "Flight Added Successfully"
#     }


# @router.get("/")
# def get_flights(
#     db: Session = Depends(get_db)
# ):

#     return fetch_flights(db)






# @router.get("/{flight_id}")
# def get_flight(
#     flight_id: int,
#     db: Session = Depends(get_db)
# ):

#     flight = fetch_flight_by_id(
#         db,
#         flight_id
#     )

#     if not flight:
#         return {
#             "message": "Flight Not Found"
#         }

#     return flight



# @router.delete("/{flight_id}")
# def delete_flight_api(
#     flight_id: int,
#     db: Session = Depends(get_db)
# ):

#     deleted = remove_flight(
#         db,
#         flight_id
#     )

#     if not deleted:
#         return {
#             "message": "Flight Not Found"
#         }

#     return {
#         "message": "Flight Deleted Successfully"
#     }





from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

# from app.schemas.flight_schema import FlightCreate


from app.schemas.flight_schema import (
    FlightCreate,
    FlightUpdate
)


from app.core.security import admin_required



# from app.services.flight_service import (
#     add_flight,
#     fetch_flights,
#     fetch_flight_by_id,
#     remove_flight
# )

from app.services.flight_service import (
    add_flight,
    fetch_flights,
    fetch_flight_by_id,
    remove_flight,
    search_flight_service,
    update_flight_service
)

router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


# @router.post("/")
# def create_new_flight(
#     request: FlightCreate,
#     db: Session = Depends(get_db)
# ):
@router.post("/")
def create_new_flight(
    request: FlightCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    add_flight(
        db,
        request
    )

    return {
        "message": "Flight Added Successfully"
    }


@router.get("/")
def get_flights(
    db: Session = Depends(get_db)
):

    return fetch_flights(db)


@router.get("/{flight_id}")
def get_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    flight = fetch_flight_by_id(
        db,
        flight_id
    )

    if not flight:
        return {
            "message": "Flight Not Found"
        }

    return flight


# @router.delete("/{flight_id}")
# def delete_flight_api(
#     flight_id: int,
#     db: Session = Depends(get_db)
# ):

@router.delete("/{flight_id}")
def delete_flight_api(
    flight_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):



    deleted = remove_flight(
        db,
        flight_id
    )

    if not deleted:
        return {
            "message": "Flight Not Found"
        }

    return {
        "message": "Flight Deleted Successfully"
    }




@router.get("/search/")
def search_flight_api(
    source: str,
    destination: str,
    db: Session = Depends(get_db)
):

    return search_flight_service(
        db,
        source,
        destination
    )





# @router.put("/{flight_id}")
# def update_flight_api(
#     flight_id: int,
#     request: FlightUpdate,
#     db: Session = Depends(get_db)
# ):
@router.put("/{flight_id}")
def update_flight_api(
    flight_id: int,
    request: FlightUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):



    flight = update_flight_service(
        db,
        flight_id,
        request
    )

    if not flight:
        return {
            "message": "Flight Not Found"
        }

    return {
        "message": "Flight Updated Successfully"
    }





