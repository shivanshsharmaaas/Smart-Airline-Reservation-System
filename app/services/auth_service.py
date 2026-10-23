from sqlalchemy.orm import Session

from app.models.user import User

from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)

from app.core.security import hash_password


def register_user(
    db: Session,
    name: str,
    email: str,
    password: str
):

    existing_user = get_user_by_email(
        db,
        email
    )

    if existing_user:
        return None

    new_user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    return create_user(
        db,
        new_user
    )




from app.core.security import verify_password


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
        db,
        email
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    return user


from app.core.security import create_access_token


def generate_login_token(user):

    token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )

    return token



    