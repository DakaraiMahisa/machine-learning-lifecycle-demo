from fastapi import APIRouter

from app.ml.predictor import (
    predict_machine_status,
)
from app.models.prediction_models import (
    PredictionRequest,
    PredictionResponse,
)

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)

@router.post(
    "/",
    response_model=PredictionResponse,
)
def predict(
    request: PredictionRequest,
):
    """
    Predict machine health status.
    """

    prediction = predict_machine_status(
        temperature=request.temperature,
        humidity=request.humidity,
        voltage=request.voltage,
        vibration=request.vibration,
    )

    return PredictionResponse(
        prediction=prediction
    )