from rankvision.keepa_client import KeepaClient
from rankvision.data_manager import DataManager
from rankvision.model import ForecastModel
from rankvision.report import ReportGenerator

class RankVisionPipeline:
    def __init__(self, keepa_key):
        self.client = KeepaClient(keepa_key)
        self.model = ForecastModel()

    def run(self, asin: str):
        raw = self.client.get_product_data(asin)
        data = DataManager(raw).preprocess()
        forecast = self.model.predict_trend(data["salesRank"].tolist())
        report = ReportGenerator(data)
        report.generate_plot()
        return {"forecast": forecast, "summary": report.summary()}
