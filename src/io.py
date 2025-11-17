from pathlib import Path
import pandas as pd

# Path to the folder that contains the whole project (schedule-tool)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_schedule_input(filename: str) -> pd.DataFrame:
    """Load the Excel input file from data/raw."""
    path = DATA_DIR / "raw" / filename
    print("Loading from:", path)  # optional debug
    return pd.read_excel(path)


def save_schedule_output(df: pd.DataFrame, filename: str) -> None:
    """Save the schedule result to data/output."""
    path = DATA_DIR / "output" / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    print("Saving to:", path)  # optional debug
    df.to_excel(path, index=False)
