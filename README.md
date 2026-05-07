# machine-learning-lifecycle-demo

A mini web platform that demonstrates the complete ML workflow using simulated industrial sensor data.

# ML Lifecycle Demo

A comprehensive demonstration of machine learning lifecycle management, including data processing, model training, deployment, and monitoring.

## Project Structure

```
ml-lifecycle-demo/
│
├── app/                    # Main application code
│   ├── api/               # API endpoints and routes
│   ├── core/              # Core configuration and utilities
│   ├── ml/                # Machine learning pipeline
│   ├── services/          # Business logic services
│   ├── models/            # Data models and schemas
│   └── main.py            # Application entry point
│
├── data/                  # Data storage directory
├── static/                # Static files (CSS, JS, etc.)
├── tests/                 # Test suite
│
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker container configuration
├── docker-compose.yml    # Multi-container orchestration
├── .dockerignore         # Docker build ignore patterns
├── .gitignore            # Git ignore patterns
└── README.md             # This file
```

## Getting Started

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional)
- pip or conda

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ml-lifecycle-demo
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running Locally

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Running with Docker

```bash
docker-compose up --build
```

## API Endpoints

- `GET /` - Health check
- `GET /health` - Application health status

## Testing

Run the test suite:

```bash
pytest
```

With coverage:

```bash
pytest --cov=app tests/
```

## Development

### Directory Descriptions

- **app/api/**: FastAPI route handlers and endpoint definitions
- **app/core/**: Configuration, constants, and utility functions
- **app/ml/**: ML pipeline, model training, and inference logic
- **app/services/**: Business logic and data processing services
- **app/models/**: Pydantic models and database schemas
- **data/**: Raw and processed data storage
- **static/**: Frontend assets and static resources
- **tests/**: Unit and integration tests

## Configuration

Create a `.env` file in the root directory for environment variables:

```
DEBUG=False
LOG_LEVEL=INFO
```

## License

MIT

## Authors

Your Name or Organization
