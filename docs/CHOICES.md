# CHOICES.md

# Technical Design Decisions

This document explains the key architectural and implementation decisions made during the development of the AI-Powered Retail Store Intelligence Platform.

The project was built using an AI-assisted engineering workflow, where design alternatives were evaluated before selecting the final implementation.

---

# Decision 1: Object Detection Model

## Options Considered

### YOLOv8

Pros:

* Fast inference
* Lightweight deployment
* Excellent community support
* Easy integration

### Faster R-CNN

Pros:

* High accuracy

Cons:

* Slower inference
* Higher resource requirements

### RT-DETR

Pros:

* Modern transformer-based architecture

Cons:

* More complex setup
* Limited development time

---

## AI-Assisted Evaluation

Multiple model options were evaluated based on:

* Detection accuracy
* Inference speed
* Ease of deployment
* CPU compatibility

The AI-assisted evaluation consistently favored YOLOv8 for rapid development and real-time retail analytics.

---

## Final Choice

YOLOv8n

---

## Rationale

The challenge prioritized practical deployment and event generation rather than maximizing benchmark accuracy.

YOLOv8n provides:

* Fast inference
* Lightweight execution
* Strong person detection performance
* Easy deployment in Docker environments

This made it the most suitable choice for a hackathon-scale implementation.

---

# Decision 2: Event Data Model

## Options Considered

### Option A

Store raw detection outputs directly.

Example:

```json
{
  "camera_id": "cam1",
  "person_count": 4
}
```

### Option B

Convert detections into structured business events.

Example:

```json
{
  "event_id": "e1",
  "store_id": "purplle_001",
  "visitor_id": "v1",
  "event_type": "person_entered"
}
```

---

## AI-Assisted Evaluation

The AI-assisted analysis recommended an event-driven architecture because analytics systems operate more effectively on business events than raw detections.

---

## Final Choice

Structured Event Schema

---

## Rationale

Each event contains:

* event_id
* store_id
* visitor_id
* camera_id
* event_type
* timestamp
* metadata

Benefits:

* Decouples detection from analytics
* Simplifies aggregation queries
* Supports future streaming pipelines
* Enables scalable analytics services

This approach closely resembles production-grade data engineering architectures.

---

# Decision 3: Backend Framework

## Options Considered

### Flask

Pros:

* Lightweight
* Simple

Cons:

* Manual API documentation

### Django

Pros:

* Feature rich

Cons:

* Heavyweight for microservices

### FastAPI

Pros:

* High performance
* Automatic OpenAPI generation
* Built-in validation

---

## AI-Assisted Evaluation

FastAPI was recommended because it provides strong developer productivity while maintaining excellent runtime performance.

---

## Final Choice

FastAPI

---

## Rationale

Benefits:

* Automatic Swagger UI
* OpenAPI support
* Request validation
* Type safety
* Rapid development

These features accelerated implementation while improving API quality.

---

# Decision 4: Database Architecture

## Options Considered

### SQLite

Pros:

* Zero configuration
* Lightweight
* Easy local development

Cons:

* Limited scalability
* Not suitable for cloud production workloads

### PostgreSQL

Pros:

* Production ready
* Persistent cloud storage
* Advanced querying
* Scalable architecture

Cons:

* Additional setup

### MongoDB

Pros:

* Flexible schema

Cons:

* Less suitable for analytical aggregations

---

## Final Choice

PostgreSQL

---

## Rationale

The project initially used SQLite during local development.

For deployment and evaluation, PostgreSQL was selected because it provides:

* Persistent cloud storage
* Reliable concurrent access
* Better scalability
* Production-grade database capabilities

The application is deployed on Render using a managed PostgreSQL instance.

---

# Decision 5: Analytics Architecture

## Options Considered

### Direct Querying

Calculate analytics directly from raw events.

### Pre-Aggregated Metrics

Maintain separate analytical tables.

---

## Final Choice

Direct Querying

---

## Rationale

The dataset size for the hackathon is relatively small.

Direct querying:

* Reduced implementation complexity
* Improved development speed
* Kept architecture simple

For larger deployments, analytical aggregations and materialized views would be introduced.

---

# Decision 6: Deployment Strategy

## Options Considered

### Local Only

Simple but difficult for judges to evaluate.

### Cloud Deployment

Publicly accessible API environment.

---

## Final Choice

Cloud Deployment on Render

---

## Rationale

Benefits:

* Public API access
* Easy evaluation
* No local setup required
* Demonstrates production readiness

This significantly improves the reviewer experience.

---

# Future Improvements

Potential future enhancements include:

* Visitor re-identification
* Multi-store analytics
* Kafka event streaming
* Real-time dashboards
* Predictive analytics
* Customer journey tracking
* Distributed processing architecture

---

# Conclusion

The final architecture prioritizes simplicity, maintainability, and rapid delivery while maintaining a clear migration path toward enterprise-scale retail analytics. The selected technologies provide an effective balance between development speed, production readiness, and extensibility.
