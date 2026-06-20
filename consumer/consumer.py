from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "news_stream",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer started...")

for message in consumer:

    article = message.value

    print("\n===================")
    print("NEWS RECEIVED")
    print("===================")

    print(f"ID: {article['id']}")
    print(f"Title: {article['title']}")
    print(f"Timestamp: {article['timestamp']}")