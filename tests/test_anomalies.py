from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_anomalies_endpoint():
    response = client.get("/stores/purplle_001/anomalies")

    assert response.status_code == 200