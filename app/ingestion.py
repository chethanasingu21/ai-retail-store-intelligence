from sqlalchemy.orm import Session

from app.models import Event


def save_event(db: Session, event):

    db_event = Event(
        event_id=event.event_id,
        store_id=event.store_id,
        visitor_id=event.visitor_id,
        camera_id=event.camera_id,
        event_type=event.event_type,
        timestamp=event.timestamp,
        event_metadata=event.metadata
    )

    db.add(db_event)
    db.commit()