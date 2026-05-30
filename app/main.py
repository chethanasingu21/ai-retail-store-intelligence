from app.database import Base
from app.database import engine
from app.database import SessionLocal

from app.schemas import IngestRequest
from app.ingestion import save_event
from app.models import Event

from fastapi import FastAPI
from app.metrics import get_store_metrics
from app.funnel import get_store_funnel
from app.heatmap import get_heatmap
from app.anomalies import get_anomalies

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Store Intelligence API")


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/events/ingest")
def ingest(payload: IngestRequest):

    db = SessionLocal()

    accepted = 0

    for event in payload.events:
        save_event(db, event)
        accepted += 1

    db.close()

    return {
        "accepted": accepted,
        "rejected": 0
    }


@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str):

    db = SessionLocal()

    result = get_store_metrics(
        db=db,
        store_id=store_id
    )

    db.close()

    return result


@app.get("/stores/{store_id}/funnel")
def funnel(store_id: str):

    db = SessionLocal()

    result = get_store_funnel(
        db=db,
        store_id=store_id
    )

    db.close()

    return result


@app.get("/stores/{store_id}/heatmap")
def heatmap(store_id: str):

    db = SessionLocal()

    result = get_heatmap(db, store_id)

    db.close()

    return result


@app.get("/stores/{store_id}/anomalies")
def anomalies(store_id: str):

    db = SessionLocal()

    result = get_anomalies(
        db=db,
        store_id=store_id
    )

    db.close()

    return result


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "store-intelligence-api"
    }