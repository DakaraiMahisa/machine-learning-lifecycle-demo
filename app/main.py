from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from fastapi.middleware.cors import CORSMiddleware

from app.routes.prediction import router as prediction_router

app = FastAPI(
    title="ML Lifecycle Demo",
    version="1.0.0",
)

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

# Register routes
app.include_router(prediction_router)

@app.get("/")
def serve_frontend():
    return FileResponse(
        "static/index.html"
    )

@app.get("/")
def health_check():
    return {
        "status": "running"
    }