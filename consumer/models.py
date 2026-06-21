from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class NewsAnalysis(Base):

    __tablename__ = "news_analysis"

    id = Column(Integer, primary_key=True)

    news_id = Column(String)

    title = Column(Text)

    prediction = Column(String)

    confidence = Column(Float)

    explanation = Column(Text)

    blockchain_hash = Column(Text)