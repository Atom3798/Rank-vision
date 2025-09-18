import pandas as pd

class DataManager:
    def __init__(self, df: pd.DataFrame):
        if "timestamp" not in df.columns:
            raise ValueError("DataFrame must include a 'timestamp' column.")
        self.df = df.copy()

    def preprocess(self) -> pd.DataFrame:
        df = self.df.copy()
        df = df.sort_values("timestamp").drop_duplicates("timestamp")
        df["salesRank"] = pd.to_numeric(df["salesRank"], errors="coerce")
        df = df.dropna(subset=["salesRank"])
        df["rank_change"] = df["salesRank"].diff()
        df["rank_ma7"] = df["salesRank"].rolling(window=7, min_periods=1).mean()
        df["rank_ma30"] = df["salesRank"].rolling(window=30, min_periods=1).mean()
        return df

    def to_features(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        out["dayofweek"] = out["timestamp"].dt.dayofweek
        out["is_weekend"] = out["dayofweek"].isin([5, 6]).astype(int)
        return out
