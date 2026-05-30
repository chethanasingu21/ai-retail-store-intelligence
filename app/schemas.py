from datetime import datetime
from typing import Dict

from pydantic import BaseModel


class EventSchema(BaseModel):
    event_id: str
    store_id: str
    visitor_id: str
    camera_id: str
    event_type: str
    timestamp: datetime
    metadata: Dict = {}


class IngestRequest(BaseModel):
    events: list[EventSchema]


class IngestResponse(BaseModel):
    accepted: int
    rejected: int