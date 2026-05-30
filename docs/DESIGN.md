# DESIGN.md

# Store Intelligence Platform - System Design

## Overview

The Store Intelligence Platform is an AI-powered retail analytics system that converts CCTV video streams into actionable business insights.

The solution processes footage from multiple store cameras, detects customer presence using computer vision, generates structured events, stores them in a database, and exposes analytics APIs for operational monitoring.

The objective is to help retail operators understand customer behavior, store traffic patterns, zone popularity, and operational anomalies.

---

# Architecture

CCTV Cameras (CAM1–CAM5)

↓

YOLOv8 Person Detection

↓

Event Generation Pipeline

↓

FastAPI Event Ingestion API

↓

SQLite Database

↓

Analytics Layer

- Metrics
- Funnel
- Heatmap
- Anomalies

↓

Business Insights

---

# Detection Pipeline

The pipeline processes video frames using OpenCV.

Every 30th frame is passed through a YOLOv8 model.

Detected people are converted into retail events containing:

- store_id
- visitor_id
- camera_id
- timestamp
- event_type
- zone

These events are sent to the backend using the ingestion endpoint.

---

# Data Storage

SQLite was selected for simplicity and fast development.

Events are stored in a structured format and queried through SQLAlchemy ORM.

The schema supports:

- Event tracking
- Visitor analytics
- Zone analytics
- Funnel analytics

---

# Analytics APIs

The platform exposes REST APIs for:

## Metrics

Provides:

- Footfall
- Unique visitors
- Visitors currently inside

## Funnel

Provides customer journey visibility:

- Entered
- Engaged
- Checkout
- Purchased

## Heatmap

Provides zone-level visitor activity.

## Anomalies

Detects unusual operational conditions.

---

# Scalability Considerations

The current implementation uses SQLite and a single FastAPI service.

For production deployment the following upgrades would be recommended:

- PostgreSQL
- Kafka event streaming
- Distributed inference workers
- Redis caching
- Kubernetes deployment

---

# AI-Assisted Decisions

AI tools were used to accelerate architecture exploration, API design, and implementation planning.

Several approaches were evaluated with AI assistance including:

- YOLOv8 vs alternative object detectors
- Event schema design
- Analytics API structure
- Database organization

The final implementation decisions were reviewed and adapted manually based on project constraints, development speed, and deployment simplicity.

AI was used as a productivity accelerator rather than a replacement for engineering judgment.

---

# Conclusion

The system successfully transforms CCTV footage into structured retail intelligence through computer vision, event processing, analytics APIs, and operational monitoring.