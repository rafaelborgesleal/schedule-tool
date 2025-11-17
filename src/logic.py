import pandas as pd

def compute_schedule(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    if {"ProcessTime_min", "BatchSize"}.issubset(result.columns):
        result["TotalTime_min"] = result["ProcessTime_min"] * result["BatchSize"]

    return result
