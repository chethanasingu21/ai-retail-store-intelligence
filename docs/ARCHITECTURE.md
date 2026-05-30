# System Architecture

## High-Level Architecture

The Store Intelligence Platform consists of five major layers:

1. CCTV Video Layer
2. AI Detection Layer
3. Event Processing Layer
4. Data Storage Layer
5. Analytics Layer

---

## Architecture Flow

CCTV Cameras

↓

YOLOv8 Detection Engine

↓

Event Generator

↓

FastAPI Backend

↓

SQLite Database

↓

Analytics Services

* Metrics API
* Funnel API
* Heatmap API
* Anomaly API

---

## CCTV Video Layer

Input videos are captured from multiple store cameras.

Current implementation:

* CAM 1 → Skincare
* CAM 2 → Makeup
* CAM 3 → Entrance
* CAM 4 → Stockroom
* CAM 5 → Checkout

The system processes video frames at fixed intervals to optimize inference performance.

---

## AI Detection Layer

YOLOv8 is used for person detection.

Responsibilities:

* Read video frames
* Detect people
* Count visitors
* Generate structured events

Example:

{
"camera_id": "cam1",
"zone": "skincare",
"people_detected": 4
}

---

## Event Processing Layer

Detected activities are converted into events.

Example:

{
"event_id": "uuid",
"store_id": "purplle_001",
"camera_id": "cam1",
"event_type": "zone_visit"
}

Events are sent to the FastAPI ingestion endpoint.

---

## Data Storage Layer

SQLite is used as the primary datastore.

Stored information includes:

* Event identifiers
* Visitor identifiers
* Camera metadata
* Event timestamps
* Zone information

---

## Analytics Layer

Metrics Service

Provides:

* Footfall
* Unique visitors
* Visitors currently inside

Heatmap Service

Provides:

* Zone popularity analysis

Anomaly Service

Provides:

* Queue spike detection
* High visitor volume alerts

Funnel Service

Provides:

* Entered
* Engaged
* Checkout
* Purchased

---

## Deployment Architecture

Docker Compose orchestrates the application.

Components:

* FastAPI Application Container
* SQLite Database
* YOLO Processing Pipeline

The platform can be deployed locally or extended to cloud infrastructure.
