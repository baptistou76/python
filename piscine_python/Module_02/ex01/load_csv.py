import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    This function opens a csv file, check its validity,
    displays its shape and content, and return a pandas.DataFrame
    """
    try:
        if not isinstance(path, str):
            print("Error: Path must be a string")
            return None
        df = pd.read_csv(path)
        if df.empty:
            print("Error: empty csv file")
            return None
        if df.isnull().all().all():
            print("Error: csv contains only null values")
            return None
        if df.shape[1] < 2:
            print("Error: not enough columns for a csv")
            return None
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print("Error:", e)
        return None
