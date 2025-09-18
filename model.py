import pandas as pd
import numpy as np
from typing import Literal

class ForecastModel:
    """Baseline forecaster as a placeholder for a Transformer time-series model.
    Predicts short-term trend: 'Uptrend', 'Downtrend', or 'Flat'.
    """
    def __init__(self):
        pass

    def predict_trend(self, sales_rank_series: pd.Series) -> Literal["Uptrend", "Downtrend", "Flat"]:
        if len(sales_rank_series) < 5:
            return "Flat"
        recent = sales_rank_series.tail(30)
        x = np.arange(len(recent))
        slope = np.polyfit(x, recent.values, 1)[0]
        if slope < -0.1:
            return "Uptrend"
        elif slope > 0.1:
            return "Downtrend"
        return "Flat"
