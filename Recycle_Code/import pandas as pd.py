import pandas as pd
import numpy as np

class DataManager:
    def __init__(self, raw_data: pd.DataFrame):
        self.raw = raw_data

    def preprocess(self) -> pd.DataFrame:
        df = self.raw.copy()
        df.fillna(method="ffill", inplace=True)
        df["rank_change"] = df["salesRank"] - df["salesRank"].shift(1)
        return df.dropna()
