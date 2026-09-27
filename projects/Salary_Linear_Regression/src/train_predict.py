"""
Salary Prediction - Simple Linear Regression Pipeline
======================================================
This module provides an end-to-end Machine Learning pipeline to:
1. Load and validate experience-salary dataset
2. Perform exploratory data checks and split data into train/test sets
3. Train a Simple Linear Regression model (y = mx + c)
4. Evaluate performance with R2 Score, Mean Squared Error (MSE), and RMSE
5. Make predictions on new years of experience
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def train_salary_model(
    data_path: str = "data/raw/Salary_Data.csv",
    test_size: float = 0.2,
    random_state: int = 42
):
    """
    Train and evaluate a Linear Regression model on Years of Experience vs Salary.
    """
    if not os.path.exists(data_path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        alt_data_path = os.path.join(base_dir, "..", data_path)
        if os.path.exists(alt_data_path):
            data_path = alt_data_path

    print(f"[*] Loading salary dataset from: {data_path}")
    df = pd.read_csv(data_path)

    # Feature extraction
    X = df[["YearsExperience"]].values
    y = df["Salary"].values

    # Train / Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Fit model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Evaluation
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)
    mae_test = mean_absolute_error(y_test, y_pred_test)
    mse_test = mean_squared_error(y_test, y_pred_test)
    rmse_test = np.sqrt(mse_test)

    print("\n================ Model Evaluation ================")
    print(f"Model Equation : Salary = {model.coef_[0]:.2f} * (YearsExperience) + {model.intercept_:.2f}")
    print(f"Train R² Score : {r2_train:.4f}")
    print(f"Test R² Score  : {r2_test:.4f}")
    print(f"Test MAE       : ${mae_test:,.2f}")
    print(f"Test RMSE      : ${rmse_test:,.2f}")
    print("==================================================\n")

    return model, {
        "r2_train": r2_train,
        "r2_test": r2_test,
        "mae": mae_test,
        "rmse": rmse_test,
        "slope": model.coef_[0],
        "intercept": model.intercept_
    }


def predict_salary(model: LinearRegression, years: float) -> float:
    """Predict expected salary given years of experience."""
    prediction = model.predict(np.array([[years]]))[0]
    print(f"Predicted salary for {years} years experience: ${prediction:,.2f}")
    return prediction


if __name__ == "__main__":
    trained_model, metrics = train_salary_model()
    # Sample predictions
    predict_salary(trained_model, 3.5)
    predict_salary(trained_model, 7.0)
    predict_salary(trained_model, 12.0)
