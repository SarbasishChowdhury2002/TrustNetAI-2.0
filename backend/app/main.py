from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine
from app.database.models import Base

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.database.models import NewsAnalysis
from app.database.schemas import NewsCreate

from app.api.news import router as news_router
from app.api.stats import router as stats_router



# Create tables
#Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TrustNetAI 2.0"
)

app.include_router(news_router)
app.include_router(stats_router)

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

'''
@app.get("/news")
def get_news(
    db: Session = Depends(get_db)
):

    records = db.query(NewsAnalysis).all()

    return records


@app.get("/news/{news_id}")
def get_news_by_id(
    news_id: str,
    db: Session = Depends(get_db)
):

    record = (
        db.query(NewsAnalysis)
        .filter(NewsAnalysis.news_id == news_id)
        .first()
    )

    if not record:
        return {
            "error": "News not found"
        }

    return record


@app.get("/stats")
def get_stats(
    db: Session = Depends(get_db)
):

    total = db.query(NewsAnalysis).count()

    fake_count = (
        db.query(NewsAnalysis)
        .filter(NewsAnalysis.prediction == "FAKE")
        .count()
    )

    real_count = (
        db.query(NewsAnalysis)
        .filter(NewsAnalysis.prediction == "REAL")
        .count()
    )

    return {
        "total_news": total,
        "fake_news": fake_count,
        "real_news": real_count
    }
'''

