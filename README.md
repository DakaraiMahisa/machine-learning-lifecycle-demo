# Machine Learning Lifecycle Demo

A production-style end-to-end machine learning web application that demonstrates the complete ML lifecycle using simulated industrial IoT sensor data.

This project showcases:

- Data generation
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Model serialization
- ML inference APIs
- Frontend integration
- Dockerized deployment
- Public exposure using ngrok

Built using:

- FastAPI
- Scikit-learn
- Docker
- HTML/CSS/JavaScript
- Random Forest Classification

---

# Project Overview

This application simulates an industrial machine monitoring platform where sensor readings are analyzed using machine learning to predict machine health conditions.

The ML model predicts one of the following statuses:

- `NORMAL`
- `WARNING`
- `FAILURE`

The project demonstrates how machine learning systems move from:

- raw data
  to
- deployable inference applications.

---

# Features

## Machine Learning Lifecycle

### Data Collection

Synthetic industrial IoT sensor data generation:

- Temperature
- Humidity
- Voltage
- Vibration

### Data Preprocessing

- Duplicate removal
- Missing value handling
- Feature scaling
- Train-test split

### Model Training

- Random Forest Classifier
- Scikit-learn training pipeline

### Model Evaluation

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Model Deployment

- FastAPI REST APIs
- Swagger Documentation
- Dockerized application
- Public ngrok deployment

---

# Tech Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| Backend          | FastAPI               |
| ML Framework     | Scikit-learn          |
| Language         | Python 3.11           |
| Frontend         | HTML, CSS, JavaScript |
| Containerization | Docker                |
| API Docs         | Swagger UI            |
| Deployment       | ngrok / Azure Ready   |

---

# System Architecture

```text
Frontend Dashboard
        ↓
FastAPI Routes
        ↓
Pydantic Validation
        ↓
Inference Layer
        ↓
Preprocessing Scaler
        ↓
Random Forest Model
        ↓
Prediction Response
```

---

# Project Structure

```text
machine-learning-lifecycle-demo/
│
├── app/
│   │
│   ├── api/
│   │   └── routes/
│   │       └── prediction.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── ml/
│   │   ├── data_generator.py
│   │   ├── preprocessing.py
│   │   ├── trainer.py
│   │   └── predictor.py
│   │
│   ├── models/
│   │   └── prediction_models.py
│   │
│   └── main.py
│
├── artifacts/
│   ├── model.pkl
│   └── scaler.pkl
│
├── data/
│   └── sensor_data.csv
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/machine-learning-lifecycle-demo.git

cd machine-learning-lifecycle-demo
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv

venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
APP_NAME=ML Lifecycle Demo
APP_VERSION=1.0.0

API_HOST=0.0.0.0
API_PORT=8000

DEBUG=True
```

---

# Generate Dataset

```bash
python -m app.ml.data_generator
```

This creates:

```text
data/sensor_data.csv
```

---

# Train Machine Learning Model

```bash
python -m app.ml.trainer
```

This generates:

```text
artifacts/model.pkl
artifacts/scaler.pkl
```

---

# Run Application Locally

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

Health Endpoint:

```text
http://localhost:8000/health
```

---

# Docker Deployment

## Build and Run

```bash
docker compose up --build
```

Application:

```text
http://localhost:8000
```

---

# Public Deployment Using ngrok

## Start ngrok

```bash
ngrok http 8000
```

Example output:

```text
https://abc123.ngrok-free.app
```

Your ML application is now publicly accessible.

---

# API Usage

## Prediction Endpoint

### POST `/predict/`

Request:

```json
{
  "temperature": 80,
  "humidity": 70,
  "voltage": 3.2,
  "vibration": 2.1
}
```

Response:

```json
{
  "prediction": "FAILURE"
}
```

---

# Machine Learning Workflow

## 1. Data Collection

Synthetic sensor data generation using configurable ranges.

## 2. Data Preprocessing

Data cleaning and scaling using `StandardScaler`.

## 3. Feature Engineering

Selection of:

- temperature
- humidity
- voltage
- vibration

## 4. Model Training

Random Forest classifier training using Scikit-learn.

## 5. Model Evaluation

Performance evaluation using classification metrics.

## 6. Model Deployment

Real-time inference APIs using FastAPI.

---

# Production Features

- Modular architecture
- Dockerized deployment
- Environment variable configuration
- Centralized logging
- Health check endpoints
- Artifact serialization
- Startup lifecycle management
- API validation using Pydantic
- Responsive frontend dashboard

---

# Future Improvements

- Azure deployment
- CI/CD pipeline
- Kubernetes deployment
- PostgreSQL integration
- Real sensor data ingestion
- User authentication
- Model monitoring
- Prometheus/Grafana integration
- MLflow experiment tracking
- Deep learning models
- Real-time streaming inference

---

# Learning Outcomes

This project demonstrates:

- End-to-end ML system design
- Production API architecture
- Docker containerization
- ML preprocessing pipelines
- Model serialization
- REST API engineering
- Frontend/backend integration
- Deployment workflows

---

# Screenshots

Add screenshots here:

```text
/docs screenshots/
dashboard screenshots/
prediction examples/
```

---

# Author

Developed as a hands-on demonstration of:

- Machine Learning Lifecycle
- ML Engineering
- Backend Engineering
- Docker Deployment
- FastAPI Architecture

---

# License

MIT License
