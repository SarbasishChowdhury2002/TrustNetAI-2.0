from fastapi import APIRouter
from app.database.session import SessionLocal
from app.database.models import NewsAnalysis

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/")
def get_all_news():

    db = SessionLocal()

    records = db.query(NewsAnalysis).all()

    db.close()

    return records


@router.get("/{news_id}")
def get_news(news_id: str):

    db = SessionLocal()

    record = (
        db.query(NewsAnalysis)
        .filter(NewsAnalysis.news_id == news_id)
        .first()
    )

    db.close()

    return record


@router.get("/stats/summary")
def get_stats():

    db = SessionLocal()

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

    db.close()

    return {
        "total_news": total,
        "fake_news": fake_count,
        "real_news": real_count
    }


