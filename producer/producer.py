from kafka import KafkaProducer

import json
import os
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

folder = "news_data"

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    with open(path, "r") as f:

        article = json.load(f)

        producer.send(
            "news_stream",
            article
        )

        print(
            f"Published: {article['title']}"
        )

        time.sleep(2)

producer.flush()