from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    keepa_api_key: str = os.getenv("KEEPA_API_KEY", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    domain: int = int(os.getenv("KEEPA_DOMAIN", "1"))  # 1 = US

settings = Settings()
