from pydantic import BaseModel


# class FlightCreate(BaseModel):

#     flight_number: str

#     source: str

#     destination: str

#     departure_time: str

#     arrival_time: str

#     price: float

#     available_seats: int

class FlightCreate(BaseModel):

    flight_number: str
    source: str
    destination: str
    departure_time: str
    arrival_time: str
    price: float
    available_seats: int
    status: str










class FlightUpdate(BaseModel):

    flight_number: str

    source: str

    destination: str

    departure_time: str

    arrival_time: str

    price: float

    available_seats: int
    status: str 




    




