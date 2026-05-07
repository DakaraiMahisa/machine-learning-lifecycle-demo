from dotenv import load_dotenv

import os

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "ML Lifecycle Demo",
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0",
)

API_HOST = os.getenv(
    "API_HOST",
    "0.0.0.0",
)

API_PORT = int(
    os.getenv(
        "API_PORT",
        8000,
    )
)

DEBUG = os.getenv(
    "DEBUG",
    "False",
) == "True"

TEMPERATURE_RANGE = (20, 100)
HUMIDITY_RANGE = (20, 90)
VOLTAGE_RANGE = (3.0, 5.5)
VIBRATION_RANGE = (0.1, 2.5)

DATASET_SIZE = 1000

NORMAL = "NORMAL"
WARNING = "WARNING"
FAILURE = "FAILURE"