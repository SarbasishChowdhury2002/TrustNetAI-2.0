from sqlalchemy.orm import Session

from app.database.models import NewsAnalysis


def get_all_news(db: Session):

    return db.query(NewsAnalysis).all()


def get_news_by_id(db: Session, news_id: str):

    return (
        db.query(NewsAnalysis)
        .filter(NewsAnalysis.news_id == news_id)
        .first()
    )


def get_recent_news(db: Session):

    return (
        db.query(NewsAnalysis)
        .order_by(NewsAnalysis.id.desc())
        .limit(10)
        .all()
    )


def get_recent_news(db: Session):

    return (
        db.query(NewsAnalysis)
        .order_by(NewsAnalysis.id.desc())
        .limit(10)
        .all()
    )