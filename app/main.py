from app.sales import get_sales_metrics
from app.database import Base
from app.database import engine
from app.database import SessionLocal
from app.brands import get_top_brands
from app.schemas import IngestRequest
from app.ingestion import save_event
from app.models import Event

from app.staff import get_staff_performance
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

@app.get("/stores/{store_id}/conversion")
def conversion(store_id: str):

    db = SessionLocal()

    metrics = get_store_metrics(
        db=db,
        store_id=store_id
    )

    db.close()

    sales = get_sales_metrics()

    footfall = metrics["footfall"]
    buyers = sales["buyers"]

    conversion_rate = (
        round((buyers / footfall) * 100, 2)
        if footfall > 0 else 0
    )

    return {
        "store_id": store_id,
        "footfall": footfall,
        "buyers": buyers,
        "conversion_rate": conversion_rate
    }
@app.get("/stores/{store_id}/brands")
def brands(store_id: str):

    return {
        "store_id": store_id,
        "top_brands": get_top_brands()
    }


@app.get("/stores/{store_id}/staff")
def staff(store_id: str):

    return {
        "store_id": store_id,
        "staff_performance": get_staff_performance()
    }