from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_dataset(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.
    """

    return pd.read_csv(path)

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset by handling missing values and duplicates.
    """

    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing numeric values
    numeric_columns = df.select_dtypes(include=["number"]).columns

    df[numeric_columns] = df[numeric_columns].fillna(
        df[numeric_columns].mean()
    )

    return df


def split_features_and_target(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Separate input features and target variable.
    """

    X = df.drop(columns=["status"])
    y = df["status"]

    return X, y

def split_dataset(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
):
    """
    Split dataset into training and testing sets.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42,
        stratify=y,
    )

def scale_features(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
):
    """
    Scale features using StandardScaler.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    return (
        X_train_scaled,
        X_test_scaled,
        scaler,
    )

def preprocess_pipeline(path: str):
    """
    Complete preprocessing workflow.
    """

    df = load_dataset(path)

    df = clean_dataset(df)

    X, y = split_features_and_target(df)

    X_train, X_test, y_train, y_test = split_dataset(X, y)

    (
        X_train_scaled,
        X_test_scaled,
        scaler,
    ) = scale_features(X_train, X_test)

    return {
        "X_train": X_train_scaled,
        "X_test": X_test_scaled,
        "y_train": y_train,
        "y_test": y_test,
        "scaler": scaler,
    }

if __name__ == "__main__":

    processed_data = preprocess_pipeline(
        "data/sensor_data.csv"
    )

    print("Preprocessing completed.")

    print(
        processed_data["X_train"][:5]
    )