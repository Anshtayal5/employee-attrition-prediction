import pandas as pd

from src.config import DATASET_PATH
def load_dataset():
    """
    Load the employee attrition dataset.

    Returns:
        pandas.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If the dataset is empty.
    """
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
        f"Dataset not found at: {DATASET_PATH}"
    )
    df = pd.read_csv(DATASET_PATH)
    if df.empty:
        raise ValueError("The dataset is empty.")
    return df