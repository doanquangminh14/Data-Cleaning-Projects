"""
Data Profiling & Quality Validation Utilities
"""

import pandas as pd
from typing import Dict, Any


def profile_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate summary profiling metrics for a pandas DataFrame."""
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isna().sum().sum()
    duplicate_rows = df.duplicated().sum()

    profile = {
        "num_rows": int(df.shape[0]),
        "num_columns": int(df.shape[1]),
        "duplicate_rows": int(duplicate_rows),
        "total_missing_values": int(missing_cells),
        "missing_percentage": round((missing_cells / total_cells * 100) if total_cells > 0 else 0.0, 2),
        "column_types": {col: str(dtype) for col, dtype in df.dtypes.items()}
    }
    return profile


def detect_missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame detailing null count and percentages per column."""
    null_counts = df.isna().sum()
    null_percent = (null_counts / len(df)) * 100
    summary_df = pd.DataFrame({
        "Missing_Count": null_counts,
        "Percentage (%)": null_percent.round(2)
    })
    return summary_df[summary_df["Missing_Count"] > 0].sort_values(by="Missing_Count", ascending=False)
