import random
from pathlib import Path

import pandas as pd

from app.core.config import (
    DATASET_SIZE,
    FAILURE,
    HUMIDITY_RANGE,
    NORMAL,
    TEMPERATURE_RANGE,
    VIBRATION_RANGE,
    VOLTAGE_RANGE,
    WARNING,
)

DATA_PATH = Path("data/sensor_data.csv")


def generate_sensor_reading() -> dict:
    """
    Generate a single synthetic sensor reading.
    """

    temperature = round(random.uniform(*TEMPERATURE_RANGE), 2)
    humidity = round(random.uniform(*HUMIDITY_RANGE), 2)
    voltage = round(random.uniform(*VOLTAGE_RANGE), 2)
    vibration = round(random.uniform(*VIBRATION_RANGE), 2)

    status = determine_machine_status(
        temperature=temperature,
        vibration=vibration,
        voltage=voltage,
    )

    return {
        "temperature": temperature,
        "humidity": humidity,
        "voltage": voltage,
        "vibration": vibration,
        "status": status,
    }


def determine_machine_status(
    temperature: float,
    vibration: float,
    voltage: float,
) -> str:
    """
    Determine equipment health status based on sensor values.
    """

    if temperature > 75 and vibration > 1.8:
        return FAILURE

    if temperature > 55 or vibration > 1.2 or voltage < 3.5:
        return WARNING

    return NORMAL


def generate_dataset(size: int = DATASET_SIZE) -> pd.DataFrame:
    """
    Generate synthetic dataset.
    """

    records = [generate_sensor_reading() for _ in range(size)]

    return pd.DataFrame(records)


def save_dataset(df: pd.DataFrame) -> None:
    """
    Save dataset to CSV.
    """

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(DATA_PATH, index=False)

    print(f"Dataset saved to: {DATA_PATH}")


if __name__ == "__main__":
    dataset = generate_dataset()
    save_dataset(dataset)

    print(dataset.head())