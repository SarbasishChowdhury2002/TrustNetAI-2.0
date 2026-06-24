from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.analytics_service import (
    get_summary,
    get_confidence_stats,
    get_fake_count,
    get_real_count,
    get_distribution
)

from app.services.news_service import get_recent_news

router = APIRouter(
    prefix="/stats",
    tags=["Analytics"]
)


@router.get("/")
def summary(
    db: Session = Depends(get_db)
):
    return get_summary(db)


@router.get("/confidence")
def confidence(
    db: Session = Depends(get_db)
):
    return get_confidence_stats(db)


@router.get("/fake")
def fake_news(
    db: Session = Depends(get_db)
):
    return get_fake_count(db)


@router.get("/real")
def real_news(
    db: Session = Depends(get_db)
):
    return get_real_count(db)


@router.get("/distribution")
def distribution(
    db: Session = Depends(get_db)
):
    return get_distribution(db)


@router.get("/recent")
def recent(
    db: Session = Depends(get_db)
):
    return get_recent_news(db)