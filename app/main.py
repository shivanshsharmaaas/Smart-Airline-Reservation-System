# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home():
#     return {
#         "message": "Smart Airline System Running Successfully"
#     }


from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

from app.models.user import User

from app.routes.auth_routes import router as auth_router

from app.models.flight import Flight


from app.routes.flight_routes import (
    router as flight_router
)


from app.models.booking import Booking

from app.models.waitlist import Waitlist


from app.routes.booking_routes import (
    router as booking_router
)

from app.routes.dashboard_routes import (
    router as dashboard_router
)







app = FastAPI(
    title="Smart Airline Operations Management System"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

app.include_router(flight_router)

app.include_router(booking_router)

app.include_router(
    dashboard_router
)




@app.get("/")
def home():
    return {
        "message": "Smart Airline System Running Successfully"
    }



