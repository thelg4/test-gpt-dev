import pandas as pd
from typing import Dict, Any


def load_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def get_summary_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    return df.describe(include='all').to_dict()


def get_null_counts(df: pd.DataFrame) -> Dict[str, int]:
    return df.isnull().sum().to_dict()


def get_column_types(df: pd.DataFrame) -> Dict[str, str]:
    return {col: str(dtype) for col, dtype in df.dtypes.items()}


def analyze_csv(file_path: str) -> Dict[str, Any]:
    df = load_csv(file_path)
    return {
        "summary": get_summary_statistics(df),
        "null_counts": get_null_counts(df),
        "column_types": get_column_types(df)
    }