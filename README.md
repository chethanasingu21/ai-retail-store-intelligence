# AI-Powered Retail Store Intelligence Platform

## Overview

AI-Powered Retail Store Intelligence Platform is an end-to-end retail analytics solution that transforms CCTV footage and retail sales data into actionable business intelligence.

The platform uses YOLOv8-based computer vision to detect and track customer activity inside retail stores, generates visitor events, stores them in a PostgreSQL database, and exposes business intelligence insights through FastAPI-powered analytics APIs.

Retailers can monitor customer footfall, analyze conversion funnels, identify high-performing brands, evaluate staff performance, detect operational anomalies, and optimize store layouts using zone-based heatmaps.

---

## Key Features

### Computer Vision Analytics

* YOLOv8-based customer detection
* Automated visitor counting
* Multi-camera video processing
* Event generation from CCTV footage
* Customer movement tracking

### Business Intelligence Analytics

* Footfall Analytics
* Customer Funnel Analytics
* Conversion Rate Analytics
* Zone Heatmaps
* Brand Performance Analytics
* Staff Performance Analytics
* Operational Anomaly Detection

### Platform Capabilities

* FastAPI REST APIs
* PostgreSQL Persistent Storage
* Dockerized Deployment
* Cloud Deployment on Render
* Interactive Swagger Documentation

---

## Business Impact

This platform enables retailers to:

* Measure store footfall automatically
* Track customer engagement across store zones
* Analyze customer purchase funnels
* Improve conversion rates
* Identify top-performing brands
* Evaluate staff effectiveness
* Detect unusual store activity
* Optimize store layouts and merchandising
* Improve overall customer experience

---

## System Architecture

```text
CCTV Cameras
      │
      ▼
YOLOv8 Detection Engine
      │
      ▼
Event Generator
      │
      ▼
FastAPI Backend
      │
      ▼
PostgreSQL Database
      │
      ▼
Analytics Engine
      │
      ├── Footfall Analytics
      ├── Funnel Analytics
      ├── Heatmap Analytics
      ├── Conversion Analytics
      ├── Brand Analytics
      ├── Staff Analytics
      └── Anomaly Detection
```

### Sales Intelligence Pipeline

```text
POS / Sales Data
        │
        ▼
 Analytics Engine
        │
        ├── Brand Insights
        ├── Staff Performance
        └── Conversion Analytics
```

---

## Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy

### Computer Vision

* YOLOv8
* OpenCV

### Data Processing

* Pandas
* NumPy

### Database

* PostgreSQL

### Deployment

* Docker
* Render Cloud Platform

---

## API Endpoints

### Event Ingestion

#### POST `/events/ingest`

Accepts generated visitor events from the computer vision pipeline.

Example event:

```json
{
  "event_id": "e1",
  "store_id": "purplle_001",
  "visitor_id": "v1",
  "camera_id": "cam1",
  "event_type": "person_entered",
  "timestamp": "2026-06-03T10:00:00Z",
  "metadata": {
    "zone": "entrance"
  }
}
```

---

### Analytics APIs

#### GET `/stores/{store_id}/metrics`

Returns:

* Footfall
* Unique Visitors
* Visitors Inside

Example:

```json
{
  "store_id": "purplle_001",
  "footfall": 3,
  "unique_visitors": 3,
  "visitors_inside": 3
}
```

---

#### GET `/stores/{store_id}/funnel`

Returns:

* Entered
* Engaged
* Checkout
* Purchased

Example:

```json
{
  "store_id": "purplle_001",
  "entered": 3,
  "engaged": 1,
  "checkout": 1,
  "purchased": 1
}
```

---

#### GET `/stores/{store_id}/heatmap`

Returns zone-level customer activity.

Example:

```json
{
  "store_id": "purplle_001",
  "zones": {
    "entrance": 2,
    "skincare": 2,
    "checkout": 1
  }
}
```

---

#### GET `/stores/{store_id}/conversion`

Returns:

* Footfall
* Buyers
* Conversion Rate

---

#### GET `/stores/{store_id}/brands`

Returns top-performing brands based on sales.

---

#### GET `/stores/{store_id}/staff`

Returns staff performance rankings.

---

#### GET `/stores/{store_id}/anomalies`

Returns detected operational anomalies.

---

## Demo Store

Use the following demo store:

```text
Store ID: purplle_001
```

---

## Quick Demo Guide

### Step 1

Open Swagger UI:

```text
https://ai-retail-store-intelligence.onrender.com/docs
```

### Step 2

Initialize demo data:

```text
POST /demo/reset
```

### Step 3

Run the analytics endpoints:

```text
GET /stores/purplle_001/metrics

GET /stores/purplle_001/funnel

GET /stores/purplle_001/heatmap

GET /stores/purplle_001/conversion

GET /stores/purplle_001/brands

GET /stores/purplle_001/staff

GET /stores/purplle_001/anomalies
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/chethanasingu21/ai-retail-store-intelligence.git
```

### Navigate to Project

```bash
cd ai-retail-store-intelligence
```

### Build and Start

```bash
docker compose up --build
```

### Access Swagger UI

```text
http://localhost:8000/docs
```

---

## Cloud Deployment

### Live API

```text
https://ai-retail-store-intelligence.onrender.com
```

### Swagger Documentation

```text
https://ai-retail-store-intelligence.onrender.com/docs
```

### Health Endpoint

```text
https://ai-retail-store-intelligence.onrender.com/health
```

---

## Screenshots

Include screenshots for:

* Architecture Diagram
* Swagger UI
* Metrics Analytics
* Funnel Analytics
* Heatmap Analytics
* Conversion Analytics
* Brand Analytics
* Staff Analytics
* Anomaly Detection

---

## Future Enhancements

* Real-time video stream analytics
* Multi-store centralized dashboard
* Customer journey tracking
* Predictive demand forecasting
* AI-powered staffing recommendations
* Real-time alerting and notifications
* Generative AI retail insights assistant

---

## Project Highlights

* End-to-End Retail Analytics Platform
* Computer Vision + Business Intelligence Integration
* Cloud-Native Architecture
* Persistent PostgreSQL Storage
* Production-Ready REST APIs
* Real-Time Event Processing Pipeline
* Retail-Focused Decision Intelligence

---

## Author

**Chethana Singu**
