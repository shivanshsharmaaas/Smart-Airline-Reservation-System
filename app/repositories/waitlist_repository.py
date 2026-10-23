from sqlalchemy.orm import Session

from app.models.waitlist import Waitlist


def create_waitlist(
    db: Session,
    waitlist: Waitlist
):

    db.add(waitlist)

    db.commit()

    db.refresh(waitlist)

    return waitlist


def get_waitlist_count(
    db: Session,
    flight_id: int
):

    return (
        db.query(Waitlist)
        .filter(
            Waitlist.flight_id == flight_id
        )
        .count()
    )





def get_first_waitlist(
    db: Session,
    flight_id: int
):

    return (
        db.query(Waitlist)
        .filter(
            Waitlist.flight_id == flight_id
        )
        .order_by(
            Waitlist.waitlist_no
        )
        .first()
    )


def delete_waitlist(
    db: Session,
    waitlist
):

    db.delete(waitlist)

    db.commit()



    
