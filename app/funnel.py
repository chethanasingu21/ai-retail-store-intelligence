from sqlalchemy.orm import Session

from app.models import Event


def get_store_funnel(db: Session, store_id: str):

    entered = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "person_entered"
        )
        .count()
    )

    engaged = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "product_engaged"
        )
        .count()
    )

    checkout = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "checkout_visit"
        )
        .count()
    )

    purchased = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "purchase_completed"
        )
        .count()
    )

    return {
        "store_id": store_id,
        "entered": entered,
        "engaged": engaged,
        "checkout": checkout,
        "purchased": purchased
    }