from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.models import NewsAnalysis


def get_summary(db: Session):

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


def get_confidence_stats(db: Session):

    result = (
        db.query(
            func.avg(NewsAnalysis.confidence),
            func.max(NewsAnalysis.confidence),
            func.min(NewsAnalysis.confidence)
        )
        .first()
    )

    if result[0] is None:
        return {
            "average_confidence": 0,
            "highest_confidence": 0,
            "lowest_confidence": 0
        }

    return {
        "average_confidence": round(result[0], 4),
        "highest_confidence": round(result[1], 4),
        "lowest_confidence": round(result[2], 4)
    }


def get_fake_count(db: Session):

    count = (
        db.query(NewsAnalysis)
        .filter(NewsAnalysis.prediction == "FAKE")
        .count()
    )

    return {
        "fake_news_count": count
    }


def get_real_count(db: Session):

    count = (
        db.query(NewsAnalysis)
        .filter(NewsAnalysis.prediction == "REAL")
        .count()
    )

    return {
        "real_news_count": count
    }


def get_distribution(db: Session):

    total = db.query(NewsAnalysis).count()

    if total == 0:
        return {
            "fake_percentage": 0,
            "real_percentage": 0
        }

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
        "fake_percentage": round((fake_count / total) * 100, 2),
        "real_percentage": round((real_count / total) * 100, 2)
    }