from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import (
    APP_NAME,
    APP_VERSION,
)

from app.ml.predictor import (
    load_artifacts,
)

from app.api.routes.prediction import (
    router as prediction_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup lifecycle.
    """

    load_artifacts()

    yield


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    lifespan=lifespan,
)

# Serve static frontend assets
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(prediction_router)


@app.get("/")
def serve_frontend():
    """
    Serve frontend dashboard.
    """

    return FileResponse(
        "static/index.html"
    )


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy"
    }