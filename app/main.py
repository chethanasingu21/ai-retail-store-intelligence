from fastapi import FastAPI

app = FastAPI(title="Store Intelligence API")


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/events/ingest")
def ingest():
    return {"message": "stub"}


@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str):
    return {"store_id": store_id}


@app.get("/stores/{store_id}/funnel")
def funnel(store_id: str):
    return {"store_id": store_id}


@app.get("/stores/{store_id}/heatmap")
def heatmap(store_id: str):
    return {"store_id": store_id}


@app.get("/stores/{store_id}/anomalies")
def anomalies(store_id: str):
    return {"store_id": store_id}


@app.get("/health")
def health():
    return {"status": "healthy"}