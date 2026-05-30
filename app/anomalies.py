from sqlalchemy.orm import Session

from app.models import Event


def get_anomalies(db: Session, store_id: str):

    anomalies = []

    visitor_count = (
        db.query(Event)
        .filter(Event.store_id == store_id)
        .count()
    )

    if visitor_count == 0:
        anomalies.append({
            "type": "DEAD_STORE",
            "severity": "WARN",
            "message": "No visitor activity detected"
        })

    if visitor_count > 50:
        anomalies.append({
            "type": "QUEUE_SPIKE",
            "severity": "INFO",
            "message": "High visitor volume detected"
        })

    return {
        "store_id": store_id,
        "anomalies": anomalies
    }