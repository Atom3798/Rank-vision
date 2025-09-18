from typing import List, Dict, Any
from dataclasses import dataclass
from openai import OpenAI
from .config import settings

SYSTEM_PROMPT = """
You are Rank Vision's e-commerce strategist. You give practical, specific recommendations
to improve Amazon sales rank and business growth. You must tailor advice to the provided
metrics, product context, competition, and feedback. Output a JSON object with:
  - "diagnosis": 2-4 bullet points on what's driving the trend
  - "actions": a list of objects {title, owner, effort: "low|medium|high", expected_impact: "low|medium|high", kpis}
  - "experiments": 2-3 test ideas with clear hypotheses and success metrics
  - "content_prompts": 2-3 bullet prompts the seller can use to generate ad copy or listing content later
Keep actions prioritized and realistic for small sellers.
"""

@dataclass
class RecommendationInput:
    trend: str
    summary: Dict[str, Any]
    business_goals: List[str]
    context: Dict[str, Any] | None = None
    feedback_notes: List[str] | None = None

class OpenAIRecommender:
    def __init__(self, api_key: str | None = None, model: str | None = None):
        api_key = api_key or settings.openai_api_key
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set.")
        self.client = OpenAI(api_key=api_key)
        self.model = model or settings.openai_model

    def recommend(self, payload: RecommendationInput) -> Dict[str, Any]:
        user_payload = {
            "trend": payload.trend,
            "summary": payload.summary,
            "business_goals": payload.business_goals,
            "context": payload.context or {},
            "feedback_notes": payload.feedback_notes or [],
        }
        resp = self.client.responses.create(
            model=self.model,
            response_format={"type": "json_object"},
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Data: {user_payload}"}
            ],
        )
        content = resp.output_text
        import json
        try:
            return json.loads(content)
        except Exception:
            return {"raw_text": content}
