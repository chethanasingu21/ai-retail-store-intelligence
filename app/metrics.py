from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models import Event


def get_store_metrics(db: Session, store_id: str):

    footfall = (
        db.query(Event)
        .filter(Event.store_id == store_id)
        .count()
    )

    unique_visitors = (
        db.query(func.count(func.distinct(Event.visitor_id)))
        .filter(Event.store_id == store_id)
        .scalar()
    )

    return {
        "store_id": store_id,
        "footfall": footfall,
        "unique_visitors": unique_visitors,
        "visitors_inside": unique_visitors
    }