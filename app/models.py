from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import JSON

from app.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(String, unique=True)
    store_id = Column(String)

    visitor_id = Column(String)

    camera_id = Column(String)

    event_type = Column(String)

    timestamp = Column(DateTime)

    event_metadata = Column(JSON)