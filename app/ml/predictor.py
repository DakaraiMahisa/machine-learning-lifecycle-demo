from pathlib import Path

import joblib
import numpy as np

MODEL_PATH = Path("artifacts/model.pkl")
SCALER_PATH = Path("artifacts/scaler.pkl")

def load_model():
    """
    Load trained ML model.
    """

    return joblib.load(MODEL_PATH)


def load_scaler():
    """
    Load preprocessing scaler.
    """

    return joblib.load(SCALER_PATH)



def predict_machine_status(
    temperature: float,
    humidity: float,
    voltage: float,
    vibration: float,
):
    """
    Predict machine health status.
    """

    model = load_model()

    scaler = load_scaler()

    input_data = np.array([
        [
            temperature,
            humidity,
            voltage,
            vibration,
        ]
    ])

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)

    return prediction[0]


if __name__ == "__main__":

    prediction = predict_machine_status(
        temperature=82,
        humidity=75,
        voltage=3.1,
        vibration=2.0,
    )

    print(f"Prediction: {prediction}")