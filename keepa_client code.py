import requests
import pandas as pd
from typing import Dict, Any
from .config import settings

class KeepaClient:
    BASE_URL = "https://api.keepa.com"

    def __init__(self, api_key: str | None = None, domain: int | None = None):
        self.api_key = api_key or settings.keepa_api_key
        self.domain = domain or settings.domain
        if not self.api_key:
            raise ValueError("KEEPA_API_KEY is not set.")

    def get_product_json(self, asin: str) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/product"
        params = {"key": self.api_key, "asin": asin, "domain": self.domain, "history": 1}
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        if not data.get("products"):
            raise ValueError(f"No product data returned for ASIN {asin}")
        return data["products"][0]

    def extract_rank_series(self, product_json: Dict[str, Any]) -> pd.DataFrame:
        import datetime as dt
        epoch = dt.datetime(2011, 1, 1)

        ranks_dict = product_json.get("salesRanks", {})
        if not ranks_dict:
            stats = product_json.get("stats", {})
            return pd.DataFrame([stats])

        first_cat = next(iter(ranks_dict))
        series = ranks_dict[first_cat]

        times, values = [], []
        for i in range(0, len(series), 2):
            t = series[i]
            v = series[i + 1]
            ts = epoch + pd.Timedelta(minutes=t)
            times.append(ts)
            values.append(None if v == -1 else v)

        df = pd.DataFrame({"timestamp": times, "salesRank": values}).dropna()
        df.sort_values("timestamp", inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df
