from pydantic import BaseModel

class NewsCreate(BaseModel):
    news_id: str
    title: str
    prediction: str
    confidence: float