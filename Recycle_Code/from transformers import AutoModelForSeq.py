from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

class ForecastModel:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def predict_trend(self, ranks: list) -> str:
        # toy example: classify "uptrend" vs "downtrend"
        inputs = self.tokenizer(" ".join(map(str, ranks)), return_tensors="pt")
        outputs = self.model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1).item()
        return "Uptrend" if pred == 1 else "Downtrend"
