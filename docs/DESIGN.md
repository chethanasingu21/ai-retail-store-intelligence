# DESIGN.md

# Store Intelligence Platform – System Design

## Overview

The AI-Powered Retail Store Intelligence Platform is an end-to-end retail analytics system that transforms CCTV video streams and retail sales data into actionable business intelligence.

The platform combines Computer Vision, Event-Driven Data Processing, PostgreSQL storage, and Analytics APIs to provide insights into customer behavior, store operations, sales performance, and operational efficiency.

The primary goal is to help retailers make data-driven decisions by automatically generating insights from both physical store activity and transaction data.

---

# System Architecture

The platform consists of six major layers:

1. Video Ingestion Layer
2. AI Detection Layer
3. Event Processing Layer
4. Data Storage Layer
5. Analytics Layer
6. API Consumption Layer

---

# High-Level Data Flow

CCTV Cameras

↓

YOLOv8 Detection Engine

↓

Customer Tracking & Event Generation

↓

FastAPI Event Ingestion API

↓

PostgreSQL Event Store

↓

Analytics Engine

↓

Business Intelligence APIs

↓

Retail Insights

Sales Data (POS)

↓

Analytics Engine

↓

Brand Analytics, Staff Analytics & Conversion Insights

---

# Video Ingestion Layer

Multiple CCTV cameras monitor different store zones.

Example Zones:

* Entrance
* Skincare
* Makeup
* Checkout
* Stockroom

Video streams are processed at configurable intervals to optimize inference performance while maintaining sufficient detection accuracy.

---

# AI Detection Layer

YOLOv8 is used for customer detection.

Responsibilities include:

* Person detection
* Visitor counting
* Zone activity monitoring
* Event generation

The lightweight YOLOv8n model was selected to support efficient execution in CPU-constrained environments.

Example Detection Output:

```json
{
  "camera_id": "cam1",
  "zone": "skincare",
  "people_detected": 4
}
```

---

# Event Processing Layer

Raw detections are transformed into structured business events.

Example Event:

```json
{
  "event_id": "e1",
  "store_id": "purplle_001",
  "visitor_id": "v1",
  "camera_id": "cam1",
  "event_type": "person_entered",
  "timestamp": "2026-06-03T10:00:00Z"
}
```

Supported Event Types:

* person_entered
* product_engaged
* checkout_visit
* purchase_completed

This event-driven design separates computer vision logic from analytics logic, improving maintainability and extensibility.

---

# Data Storage Layer

PostgreSQL serves as the primary datastore.

Stored Information:

* Event identifiers
* Visitor identifiers
* Camera metadata
* Event timestamps
* Event types
* Zone information

Benefits:

* Persistent storage
* Cloud deployment support
* Structured querying
* Production readiness

SQLAlchemy ORM is used to abstract database interactions.

---

# Analytics Layer

The analytics engine processes stored events and sales data to generate business intelligence.

## Store Metrics

Provides:

* Footfall
* Unique Visitors
* Visitors Inside

## Funnel Analytics

Provides:

* Entered
* Engaged
* Checkout
* Purchased

## Heatmap Analytics

Provides:

* Zone popularity
* Customer engagement hotspots

## Conversion Analytics

Provides:

* Buyers
* Conversion rate
* Customer purchase efficiency

## Brand Analytics

Provides:

* Top-performing brands
* Revenue contribution

## Staff Analytics

Provides:

* Staff rankings
* Revenue performance

## Anomaly Detection

Provides:

* Traffic spikes
* Queue build-up alerts
* Operational anomalies

---

# API Layer

Business intelligence is exposed through FastAPI REST APIs.

Available Endpoints:

* POST /events/ingest
* GET /stores/{store_id}/metrics
* GET /stores/{store_id}/funnel
* GET /stores/{store_id}/heatmap
* GET /stores/{store_id}/anomalies
* GET /stores/{store_id}/conversion
* GET /stores/{store_id}/brands
* GET /stores/{store_id}/staff

Interactive documentation is available through Swagger UI.

---

# Scalability Considerations

The current implementation is optimized for hackathon-scale deployment.

Future production enhancements may include:

* Kafka event streaming
* Redis caching
* Distributed inference workers
* Multi-store aggregation
* Kubernetes deployment
* Real-time dashboards

The event-driven architecture was intentionally designed to support these future extensions.

---

# AI-Assisted Decisions

AI tools were used throughout development as engineering assistants to accelerate research, design exploration, implementation planning, debugging, and documentation.

AI-assisted exploration was used for:

### Model Selection

Evaluated:

* YOLOv8
* Faster R-CNN
* RT-DETR

YOLOv8 was selected due to its balance of speed, simplicity, and detection quality.

### Event Schema Design

Different event representations were evaluated before selecting a structured event model.

This enabled clean separation between detection and analytics systems.

### API Architecture

Several API structures were explored before adopting REST-based analytics endpoints.

FastAPI was selected because of:

* Automatic OpenAPI generation
* Type validation
* Developer productivity

### Database Strategy

SQLite was initially used for local development.

PostgreSQL was adopted for cloud deployment to provide persistence, scalability, and production-readiness.

### Deployment Strategy

Multiple deployment approaches were considered before selecting Docker + Render due to simplicity and ease of evaluation.

### Engineering Review

All AI-generated suggestions were manually reviewed and adapted before implementation.

AI served as a productivity accelerator and design assistant rather than a replacement for engineering judgment.

---
# Schema Compatibility

The provided sample_events.jsonl schema includes additional attributes such as:

- Staff Identification
- Demographic Predictions
- Group Tracking
- Zone Metadata

The platform was intentionally designed using a flexible event-driven architecture and metadata-based schema.

This allows additional attributes to be incorporated without requiring changes to the analytics pipeline, storage layer, or API interfaces.

The architecture therefore remains compatible with future schema extensions while preserving backward compatibility.

# Conclusion

The Store Intelligence Platform successfully transforms CCTV footage and retail sales data into structured business intelligence through Computer Vision, Event Processing, PostgreSQL storage, and Analytics APIs.

The architecture balances rapid development, production readiness, and future scalability while demonstrating how Data Engineering and AI can be combined to solve real-world retail challenges.
