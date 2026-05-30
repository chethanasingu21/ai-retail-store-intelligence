from sqlalchemy.orm import Session

from app.models import Event


def get_heatmap(db: Session, store_id: str):

    events = (
        db.query(Event)
        .filter(Event.store_id == store_id)
        .all()
    )

    zones = {}

    for event in events:

        if not event.event_metadata:
            continue

        zone = event.event_metadata.get("zone")

        if not zone:
            continue

        zones[zone] = zones.get(zone, 0) + 1

    return {
        "store_id": store_id,
        "zones": zones
    }