from fastapi import APIRouter, HTTPException

from app.core.logger import logger

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

    try:

        logger.info(
            "Received prediction request"
        )

        prediction = predict_machine_status(
            temperature=request.temperature,
            humidity=request.humidity,
            voltage=request.voltage,
            vibration=request.vibration,
        )

        logger.info(
            f"Prediction generated: {prediction}"
        )

        return PredictionResponse(
            prediction=prediction
        )

    except Exception as error:

        logger.error(
            f"Prediction failed: {str(error)}"
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "Internal server error during "
                "prediction."
            ),
        )