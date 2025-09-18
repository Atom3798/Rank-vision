#Keepa API Wrapper

import requests
import pandas as pd

class KeepaClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.keepa.com"

    def get_product_data(self, asin: str) -> pd.DataFrame:
        url = f"{self.base_url}/product?key={self.api_key}&asin={asin}&domain=1"
        resp = requests.get(url).json()
        # parse rank & price history
        data = resp["products"][0]["stats"]
        return pd.DataFrame([data])
