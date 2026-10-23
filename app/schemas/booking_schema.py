from pydantic import BaseModel


class BookingCreate(BaseModel):

    flight_id: int


    