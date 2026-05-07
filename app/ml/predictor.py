from pathlib import Path

import joblib
import numpy as np

MODEL_PATH = Path("artifacts/model.pkl")
SCALER_PATH = Path("artifacts/scaler.pkl")

model = None
scaler = None


def load_artifacts():
    """
    Load ML artifacts into memory.
    """

    global model
    global scaler

    model = joblib.load(MODEL_PATH)

    scaler = joblib.load(SCALER_PATH)


def predict_machine_status(
    temperature: float,
    humidity: float,
    voltage: float,
    vibration: float,
):
    """
    Predict machine health status.
    """

    input_data = np.array([
        [
            temperature,
            humidity,
            voltage,
            vibration,
        ]
    ])

    scaled_data = scaler.transform(
        input_data
    )

    prediction = model.predict(
        scaled_data
    )

    return prediction[0]


if __name__ == "__main__":

    prediction = predict_machine_status(
        temperature=82,
        humidity=75,
        voltage=3.1,
        vibration=2.0,
    )

    print(f"Prediction: {prediction}")