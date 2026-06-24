import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from kafka import KafkaConsumer
import json
from models import NewsAnalysis
from db import SessionLocal
from shared.prediction_service import predict_news

consumer = KafkaConsumer(
    "news_stream",
    #bootstrap_servers="localhost:9092",
    bootstrap_servers="trustnet_kafka:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer started...")

for message in consumer:

    article = message.value

    print("\n===================")
    print("NEWS RECEIVED")
    print("===================")

    print("ARTICLE:", article)
    print("TITLE:", article["title"])

    db = SessionLocal()

    result = predict_news(article["title"])

    print("\nPrediction Result")
    print(result)

    record = NewsAnalysis(
        news_id=str(article["id"]),
        title=article["title"],
        prediction=result["prediction"],
        confidence=result["confidence"],
        explanation="AI Prediction Generated",
        blockchain_hash="NA"
    )

    db.add(record)

    db.commit()

    db.close()

    print("Stored in PostgreSQL")