from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from app.ml.preprocessing import preprocess_pipeline

MODEL_DIR = Path("artifacts")
MODEL_PATH = MODEL_DIR / "model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"

def train_model(
    X_train,
    y_train,
) -> RandomForestClassifier:
    """
    Train Random Forest classifier.
    """

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X_train, y_train)

    return model

def evaluate_model(
    model,
    X_test,
    y_test,
):
    """
    Evaluate trained model.
    """

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions,
    )

    report = classification_report(
        y_test,
        predictions,
    )

    matrix = confusion_matrix(
        y_test,
        predictions,
    )

    return {
        "accuracy": accuracy,
        "classification_report": report,
        "confusion_matrix": matrix,
    }

def save_artifacts(
    model,
    scaler,
) -> None:
    """
    Save trained model and scaler.
    """

    MODEL_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(model, MODEL_PATH)

    joblib.dump(scaler, SCALER_PATH)

    print(f"Model saved to: {MODEL_PATH}")

    print(f"Scaler saved to: {SCALER_PATH}")

def training_pipeline():
    """
    Complete ML training workflow.
    """

    processed_data = preprocess_pipeline(
        "data/sensor_data.csv"
    )

    X_train = processed_data["X_train"]
    X_test = processed_data["X_test"]
    y_train = processed_data["y_train"]
    y_test = processed_data["y_test"]
    scaler = processed_data["scaler"]

    model = train_model(
        X_train,
        y_train,
    )

    evaluation = evaluate_model(
        model,
        X_test,
        y_test,
    )

    save_artifacts(
        model,
        scaler,
    )

    return evaluation

if __name__ == "__main__":

    results = training_pipeline()

    print("\nModel Evaluation")
    print("-" * 40)

    print(
        f"Accuracy: {results['accuracy']:.4f}"
    )

    print("\nClassification Report:")
    print(
        results["classification_report"]
    )

    print("\nConfusion Matrix:")
    print(
        results["confusion_matrix"]
    )