# System Architecture

## Overview

The AI-Powered Retail Store Intelligence Platform is an event-driven retail analytics system that converts CCTV video streams and retail sales data into actionable business intelligence.

The solution combines Computer Vision, Data Engineering, API Services, and Analytics to provide real-time insights into customer behavior, store operations, staff performance, and sales conversion.

---

# Architecture Layers

The platform consists of six major layers:

1. Video Ingestion Layer
2. AI Detection Layer
3. Event Processing Layer
4. Data Storage Layer
5. Analytics Layer
6. API Consumption Layer

---

# End-to-End Data Flow

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

Retail Insights Dashboard / Consumers

Sales Data (POS)

↓

Analytics Engine

↓

Brand Performance, Staff Analytics & Conversion Metrics

---

# 1. Video Ingestion Layer

Multiple CCTV camera feeds capture customer movement throughout the store.

Example Zones:

* Entrance
* Skincare
* Makeup
* Checkout
* Stockroom

Video frames are processed at configurable intervals to optimize inference performance and reduce computational overhead.

---

# 2. AI Detection Layer

YOLOv8 performs person detection on incoming video frames.

Responsibilities:

* Detect customers
* Count visitors
* Track movement across zones
* Generate structured retail events

Example Detection Output:

{
"camera_id": "cam1",
"zone": "skincare",
"people_detected": 4
}

---

# 3. Event Processing Layer

Detection outputs are transformed into standardized business events.

Example:

{
"event_id": "uuid",
"store_id": "purplle_001",
"visitor_id": "v1",
"camera_id": "cam1",
"event_type": "person_entered",
"timestamp": "2026-06-03T10:00:00Z"
}

Events are sent to the FastAPI ingestion service through REST APIs.

This event-driven architecture enables scalable analytics and future integration with streaming platforms such as Kafka.

---

# 4. Data Storage Layer

PostgreSQL serves as the persistent event store.

Stored Information:

* Event IDs
* Visitor IDs
* Camera Metadata
* Zone Information
* Event Types
* Timestamps

Benefits:

* Persistent storage
* Queryable analytics
* Cloud deployment support
* Scalability for future growth

---

# 5. Analytics Layer

The analytics engine processes stored events to generate retail intelligence.

### Metrics Service

Provides:

* Footfall
* Unique Visitors
* Visitors Inside

### Funnel Analytics

Provides:

* Entered
* Engaged
* Checkout
* Purchased

### Heatmap Analytics

Provides:

* Zone Activity Distribution
* Customer Engagement Hotspots

### Anomaly Detection

Provides:

* Traffic Spikes
* Queue Build-up Detection
* Operational Alerts

### Business Analytics

Provides:

* Conversion Rate
* Top Performing Brands
* Staff Performance Ranking

---

# 6. API Consumption Layer

Business insights are exposed through FastAPI REST endpoints.

Available APIs:

* /events/ingest
* /stores/{store_id}/metrics
* /stores/{store_id}/funnel
* /stores/{store_id}/heatmap
* /stores/{store_id}/anomalies
* /stores/{store_id}/conversion
* /stores/{store_id}/brands
* /stores/{store_id}/staff

These APIs can be consumed by dashboards, reporting tools, or external retail systems.

---

# Deployment Architecture

The solution is containerized using Docker and deployed on Render.

Components:

* FastAPI Backend
* PostgreSQL Database
* YOLOv8 Processing Pipeline
* Analytics Services

Deployment Benefits:

* Cloud-hosted
* Persistent storage
* Scalable architecture
* Production-ready API access

---

# Architectural Highlights

* Event-Driven Design
* Computer Vision Powered Analytics
* PostgreSQL Persistence Layer
* REST API-Based Architecture
* Cloud Deployment on Render
* Extensible for Real-Time Streaming and Multi-Store Analytics
