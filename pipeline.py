from .keepa_client import KeepaClient
from .data_manager import DataManager
from .model import ForecastModel
from .report import ReportGenerator
from .recommender import OpenAIRecommender, RecommendationInput
from typing import Dict, Any, List

class RankVisionPipeline:
    def __init__(self, keepa_key: str | None = None):
        self.client = KeepaClient(api_key=keepa_key)
        self.model = ForecastModel()
        self.recommender = OpenAIRecommender()

    def run(self, asin: str, business_goals: List[str] | None = None,
            context: Dict[str, Any] | None = None,
            feedback_notes: List[str] | None = None) -> Dict[str, Any]:
        product_json = self.client.get_product_json(asin)
        df = self.client.extract_rank_series(product_json)

        processed = DataManager(df).preprocess()
        trend = self.model.predict_trend(processed["salesRank"])
        report = ReportGenerator(processed)
        summary = report.summary()
        report.generate_plot(f"{asin}_rank_trend.png")

        rec_input = RecommendationInput(
            trend=trend,
            summary=summary,
            business_goals=business_goals or ["Improve rank and units sold"],
            context=context or {},
            feedback_notes=feedback_notes or [],
        )
        recs = self.recommender.recommend(rec_input)

        return {
            "asin": asin,
            "trend": trend,
            "summary": summary,
            "recommendations": recs,
            "plot_path": f"{asin}_rank_trend.png",
        }
