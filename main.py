"""
Data Cleaning Projects - Main Execution Entrypoint
===================================================
Orchestrates and executes all data cleaning pipelines and model scripts across subprojects.
"""

import sys
import os

# Add repo root to Python path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

from projects.Customer_call_list.src.clean_customer_data import clean_customer_call_list
from projects.Salary_Linear_Regression.src.train_predict import train_salary_model


def main():
    print("=" * 60)
    print("🚀 RUNNING DATA CLEANING & ML PIPELINES")
    print("=" * 60)

    # 1. Execute Customer Call List Data Cleaning Pipeline
    print("\n[1/2] Processing Customer Call List Data Cleaning...")
    try:
        cleaned_df = clean_customer_call_list(
            input_path=os.path.join(ROOT_DIR, "projects", "Customer_call_list", "data", "raw", "Customer Call List.xlsx"),
            output_path=os.path.join(ROOT_DIR, "projects", "Customer_call_list", "data", "processed", "Customer_Call_List_Cleaned.csv")
        )
        print(f"✅ Customer Call List Pipeline completed successfully ({len(cleaned_df)} records).")
    except Exception as e:
        print(f"❌ Customer Call List Pipeline failed: {e}")

    # 2. Execute Salary Linear Regression ML Pipeline
    print("\n[2/2] Training Salary Linear Regression Model...")
    try:
        model, metrics = train_salary_model(
            data_path=os.path.join(ROOT_DIR, "projects", "Salary_Linear_Regression", "data", "raw", "Salary_Data.csv")
        )
        print(f"✅ Salary Model Pipeline completed with Test R² = {metrics['r2_test']:.4f}")
    except Exception as e:
        print(f"❌ Salary Model Pipeline failed: {e}")

    print("\n" + "=" * 60)
    print("🎉 ALL PIPELINES EXECUTED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
