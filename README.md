# AI-Powered Retail Store Intelligence Platform

An end-to-end retail analytics platform that transforms CCTV footage and retail sales data into actionable business intelligence using Computer Vision, Event Processing, and Analytics APIs.

## Overview

This project analyzes retail store CCTV footage using YOLOv8-based customer detection and combines the generated events with sales data to provide operational and business insights.

The platform enables retailers to track customer activity, measure conversion rates, monitor staff performance, identify top-performing brands, detect anomalies, and optimize store operations.

---

## Features

### Computer Vision Analytics

* YOLOv8 customer detection
* Automated visitor counting
* Event generation from CCTV footage
* Multi-camera processing pipeline

### Business Intelligence Analytics

* Footfall analytics
* Customer funnel analytics
* Conversion rate analytics
* Top brand performance analytics
* Staff performance analytics
* Zone heatmaps
* Operational anomaly detection

### Platform Features

* FastAPI REST APIs
* SQLite event storage
* Dockerized deployment
* Public cloud deployment on Render

---

## Architecture

CCTV Cameras
↓
YOLOv8 Detection
↓
Event Generator
↓
FastAPI Backend
↓
SQLite Database
↓
Analytics Engine
↓
Business Intelligence APIs

Sales Data (POS)
↓
Analytics Engine
↓
Brand, Staff and Conversion Insights

---

## API Endpoints

### Event Ingestion

POST /events/ingest

Accepts generated visitor events from the detection pipeline.

### Analytics APIs

GET /stores/{store_id}/metrics

Returns:

* Footfall
* Unique visitors
* Visitors inside

GET /stores/{store_id}/funnel

Returns customer funnel metrics.

GET /stores/{store_id}/heatmap

Returns store zone activity data.

GET /stores/{store_id}/anomalies

Returns detected operational anomalies.

GET /stores/{store_id}/conversion

Returns:

* Footfall
* Buyers
* Conversion rate

GET /stores/{store_id}/brands

Returns top-performing brands based on GMV.

GET /stores/{store_id}/staff

Returns staff performance ranked by GMV.

---

## Technology Stack

* Python
* FastAPI
* YOLOv8
* OpenCV
* SQLite
* Pandas
* Docker

---

## Local Setup

1. Clone the repository

git clone <repository-url>

2. Navigate to the project directory

cd store-intelligence

3. Start the application

docker compose up --build

4. Open Swagger UI

http://localhost:8000/docs

---

## Cloud Demo

Swagger Documentation:

https://ai-retail-store-intelligence.onrender.com/docs

Health Check:

https://ai-retail-store-intelligence.onrender.com/health

---

## Screenshots

Include screenshots from:

* Swagger UI
* Heatmap Analytics
* Metrics API
* Anomaly Detection
* Architecture Diagram

---

## Future Enhancements

* Real-time streaming analytics
* PostgreSQL integration
* Multi-store dashboard
* Predictive demand forecasting
* Customer journey analytics

---

## Author

Chethana Singu
Associate Data Engineer
