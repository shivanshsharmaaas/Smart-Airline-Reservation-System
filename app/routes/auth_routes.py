from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserRegister

from app.database.connection import get_db

from app.services.auth_service import register_user



from app.schemas.user_schema import (
    UserRegister,
    UserLogin
)

from app.services.auth_service import (
    register_user,
    login_user
)





router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: UserRegister,
    db: Session = Depends(get_db)
):

    user = register_user(
        db,
        request.name,
        request.email,
        request.password
    )

    if not user:
        return {
            "message": "Email already exists"
        }

    return {
        "message": "User Registered Successfully"
    }





from app.services.auth_service import (
    register_user,
    login_user,
    generate_login_token
)




# @router.post("/login")
# def login(
#     request: UserLogin,
#     db: Session = Depends(get_db)
# ):

#     user = login_user(
#         db,
#         request.email,
#         request.password
#     )

#     if not user:
#         return {
#             "message": "Invalid Credentials"
#         }

#     return {
#         "message": "Login Successful",
#         "user_id": user.id,
#         "name": user.name,
#         "email": user.email
#     }





@router.post("/login")
def login(
    request: UserLogin,
    db: Session = Depends(get_db)
):

    user = login_user(
        db,
        request.email,
        request.password
    )

    if not user:
        return {
            "message": "Invalid Credentials"
        }

    token = generate_login_token(user)

    return {
        "access_token": token,
        "token_type": "bearer"
    }






from app.core.security import verify_token




@router.get("/me")
def get_current_user(
    user=Depends(verify_token)
):

    return {
        "logged_user": user
    }


    
