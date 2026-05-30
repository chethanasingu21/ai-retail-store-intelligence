import requests
from datetime import datetime
from uuid import uuid4

def emit_person_event(
    store_id,
    camera_id,
    frame_number,
    people_count,
    zone
):

    payload = {
    "events": [
        {
            "event_id": str(uuid4()),
            "store_id": store_id,
            "visitor_id": f"visitor_{frame_number}",
            "camera_id": camera_id,
            "event_type": "zone_visit",
            "timestamp": datetime.now().isoformat(),
            "metadata": {
                "people_detected": people_count,
                "zone": zone
            }
        }
    ]
}

    response = requests.post(
        "http://localhost:8000/events/ingest",
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)