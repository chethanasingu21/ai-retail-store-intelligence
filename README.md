# Store Intelligence Platform

## Overview

Store Intelligence Platform is an AI-powered retail analytics system that transforms CCTV video feeds into actionable business insights.

The platform processes surveillance footage using YOLOv8-based person detection, generates store events in real time, stores them through a FastAPI backend, and exposes analytics APIs for operational monitoring.

The solution helps retailers understand customer traffic, zone popularity, visitor behavior, and operational anomalies.

---
## Demo Access

No authentication required.

Swagger UI:
http://localhost:8000/docs


## Problem Statement

Retail stores generate large volumes of CCTV footage, but extracting meaningful business insights from these video streams is difficult.

This project converts raw CCTV video into structured retail intelligence by:

* Detecting customer presence
* Measuring footfall
* Generating zone-based heatmaps
* Tracking visitor activity
* Detecting operational anomalies
* Providing analytics APIs for reporting

---

## Solution Architecture

CCTV Cameras (CAM1 - CAM5)

↓

YOLOv8 Person Detection

↓

Event Generation Pipeline

↓

FastAPI Backend

↓

SQLite Database

↓

Analytics Layer

* Metrics API
* Funnel API
* Heatmap API
* Anomaly API

---

## Features

### AI Detection Pipeline

* YOLOv8 person detection
* Multi-camera video processing
* Real-time event generation

### Analytics APIs

#### Metrics

Provides:

* Footfall
* Unique visitors
* Visitors currently inside store

#### Funnel

Tracks:

* Entered
* Engaged
* Checkout
* Purchased

#### Heatmap

Provides zone popularity analysis:

* Skincare
* Makeup
* Entrance
* Checkout
* Stockroom

#### Anomaly Detection

Detects:

* Queue spikes
* High visitor volume
* Low activity conditions

---

## Technology Stack

Backend

* FastAPI
* Python 3.10
* SQLAlchemy
* SQLite

AI & Computer Vision

* YOLOv8
* OpenCV
* PyTorch

Infrastructure

* Docker
* Docker Compose

---

## Project Structure

store-intelligence/

├── app/

├── pipeline/

├── data/

├── docs/

├── tests/

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

└── README.md

---

## API Endpoints

### Event Ingestion

POST /events/ingest

### Metrics

GET /stores/{store_id}/metrics

### Funnel

GET /stores/{store_id}/funnel

### Heatmap

GET /stores/{store_id}/heatmap

### Anomalies

GET /stores/{store_id}/anomalies

### Health Check

GET /health

---

## Sample Results

Metrics

* Footfall: 317
* Unique Visitors: 142

Heatmap

* Skincare: 140 visits
* Makeup: 108 visits

Anomalies

* Queue Spike Detected

---

## Future Improvements

* Multi-object tracking using ByteTrack or DeepSORT
* Real-time streaming ingestion
* PostgreSQL deployment
* Dashboard visualization
* Advanced anomaly detection
* Customer journey analytics

---

## Conclusion

This project demonstrates an end-to-end retail intelligence platform that converts CCTV video feeds into actionable business insights through AI-powered detection, event processing, and analytics services.
