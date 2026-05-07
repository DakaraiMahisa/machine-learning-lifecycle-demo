from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    temperature: float = Field(
        ...,
        example=75.5,
    )

    humidity: float = Field(
        ...,
        example=65.0,
    )

    voltage: float = Field(
        ...,
        example=3.8,
    )

    vibration: float = Field(
        ...,
        example=1.5,
    )

class PredictionResponse(BaseModel):
    prediction: str