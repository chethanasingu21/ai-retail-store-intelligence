# Design Decisions

## Overview

This document explains the key engineering decisions made during the development of the Store Intelligence Platform.

The goal was to create a scalable, modular, and extensible retail analytics solution capable of converting CCTV footage into actionable business insights.

---

## Why FastAPI?

FastAPI was selected because:

* High performance
* Automatic Swagger documentation
* Strong type validation using Pydantic
* Easy integration with Python AI pipelines

Benefits:

* Rapid development
* Self-documenting APIs
* Production-ready architecture

---

## Why SQLite?

SQLite was chosen for the hackathon implementation because:

* Zero configuration
* Lightweight deployment
* Easy local development
* No external infrastructure required

Future versions can migrate to PostgreSQL without major architectural changes.

---

## Why YOLOv8?

YOLOv8 was selected because:

* State-of-the-art object detection
* Fast inference speed
* Strong person detection accuracy
* Easy Python integration

The platform currently uses YOLOv8n for efficient CPU-based inference.

---

## Why Event-Driven Processing?

Instead of directly storing video analytics results, the system converts detections into events.

Advantages:

* Loose coupling
* Scalability
* Auditability
* Easier analytics generation

Example:

Person Detection

↓

Retail Event

↓

Analytics

This architecture enables future integration with streaming platforms such as Kafka.

---

## Why Camera-to-Zone Mapping?

Each camera is mapped to a physical retail zone.

Examples:

* CAM1 → Skincare
* CAM2 → Makeup
* CAM3 → Entrance
* CAM4 → Stockroom
* CAM5 → Checkout

This approach enables heatmap generation without requiring complex indoor positioning systems.

---

## Why Docker?

Docker was selected to ensure:

* Consistent deployment
* Environment reproducibility
* Simplified setup
* Easy portability

The entire backend can be started using a single command:

docker compose up

---

## Analytics Design

The analytics layer was separated from ingestion logic.

Components:

* Metrics Service
* Funnel Service
* Heatmap Service
* Anomaly Service

Benefits:

* Cleaner architecture
* Easier testing
* Independent evolution of analytics modules

---

## Known Limitations

Current implementation uses frame-based visitor identifiers.

This means:

* Visitor identities are not persistent
* Multiple detections may represent the same customer

Future versions will integrate:

* ByteTrack
* DeepSORT
* Multi-object tracking

to provide persistent customer tracking.

---

## Future Roadmap

Short-Term

* Real-time stream processing
* Improved anomaly detection
* Dashboard UI

Long-Term

* PostgreSQL migration
* Kafka integration
* Cloud deployment
* Advanced customer journey analytics
* Predictive retail intelligence

---

## Conclusion

The architecture prioritizes modularity, scalability, and rapid deployment while demonstrating a complete end-to-end retail intelligence workflow from CCTV footage to business analytics.
