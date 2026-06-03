from datetime import datetime

from app.models import Event


def seed_demo_data(db):

    events = [
        Event(
            event_id="e1",
            store_id="purplle_001",
            visitor_id="v1",
            camera_id="cam1",
            event_type="person_entered",
            timestamp=datetime.utcnow(),
            event_metadata={"zone": "entrance"}
        ),
        Event(
            event_id="e2",
            store_id="purplle_001",
            visitor_id="v2",
            camera_id="cam1",
            event_type="person_entered",
            timestamp=datetime.utcnow(),
            event_metadata={"zone": "entrance"}
        ),
        Event(
            event_id="e3",
            store_id="purplle_001",
            visitor_id="v3",
            camera_id="cam2",
            event_type="person_entered",
            timestamp=datetime.utcnow(),
            event_metadata={"zone": "skincare"}
        ),
        Event(
            event_id="e4",
            store_id="purplle_001",
            visitor_id="v1",
            camera_id="cam2",
            event_type="product_engaged",
            timestamp=datetime.utcnow(),
            event_metadata={"zone": "skincare"}
        ),
        Event(
            event_id="e5",
            store_id="purplle_001",
            visitor_id="v1",
            camera_id="cam3",
            event_type="checkout_visit",
            timestamp=datetime.utcnow(),
            event_metadata={"zone": "checkout"}
        ),
        Event(
            event_id="e6",
            store_id="purplle_001",
            visitor_id="v1",
            camera_id="cam4",
            event_type="purchase_completed",
            timestamp=datetime.utcnow(),
            event_metadata={"amount": 500}
        )
    ]

    db.add_all(events)
    db.commit()