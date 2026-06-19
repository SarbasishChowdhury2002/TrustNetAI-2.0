from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine
from app.database.models import Base

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.database.models import NewsAnalysis
from app.database.schemas import NewsCreate

# Create tables
#Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TrustNetAI 2.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "TrustNetAI 2.0"
    }

@app.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        return {
            "database": "connected"
        }

    except Exception as e:
        return {
            "database": "error",
            "details": str(e)
        }
    

@app.post("/news")
def create_news(
    news: NewsCreate,
    db: Session = Depends(get_db)
):

    record = NewsAnalysis(
        news_id=news.news_id,
        title=news.title,
        prediction=news.prediction,
        confidence=news.confidence
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return {
        "message": "stored",
        "id": record.id
    }


@app.get("/news")
def get_news(
    db: Session = Depends(get_db)
):

    records = db.query(NewsAnalysis).all()

    return records


