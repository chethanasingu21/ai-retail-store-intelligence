# CHOICES.md

# Key Technical Decisions

This document explains major architectural decisions made during implementation.

---

# Decision 1: Detection Model

## Options Considered

- YOLOv8
- Faster R-CNN
- RT-DETR

## AI Recommendation

AI-assisted exploration suggested YOLOv8 because it provides a strong balance between speed, simplicity, and accuracy.

## Final Choice

YOLOv8

## Why

The challenge required rapid development and real-time inference.

YOLOv8 offers:

- Easy setup
- Strong community support
- Fast inference
- Good person detection performance

The lightweight YOLOv8n model was selected because it performs well on CPU-only environments.

---

# Decision 2: Event Schema

## Options Considered

Option A:

Store raw detections only.

Option B:

Convert detections into structured retail events.

## AI Recommendation

AI suggested using structured events because analytics become significantly easier.

## Final Choice

Structured Event Schema

Each event contains:

- event_id
- store_id
- visitor_id
- camera_id
- event_type
- timestamp
- metadata

## Why

The event-based design separates detection from analytics.

Analytics APIs can evolve independently without changing the detection pipeline.

This architecture also mirrors production data engineering systems.

---

# Decision 3: Backend Architecture

## Options Considered

- Flask
- Django
- FastAPI

## AI Recommendation

FastAPI was recommended because of automatic OpenAPI generation and strong developer productivity.

## Final Choice

FastAPI

## Why

Benefits included:

- Automatic Swagger UI
- Type validation
- Fast development
- Clean API design

This reduced development effort and improved maintainability.

---

# Decision 4: Database Choice

## Options Considered

- SQLite
- PostgreSQL
- MongoDB

## Final Choice

SQLite

## Why

The challenge focused on functionality rather than large-scale deployment.

SQLite provided:

- Zero configuration
- Fast setup
- Easy Docker integration

For production environments PostgreSQL would be the preferred replacement.

---

# Future Improvements

Future versions could include:

- Visitor re-identification
- Real-time streaming analytics
- PostgreSQL
- Kafka
- Streamlit dashboard
- Multi-store aggregation

---

# Conclusion

The selected architecture prioritized simplicity, maintainability, and rapid delivery while preserving a clear path toward production scalability.