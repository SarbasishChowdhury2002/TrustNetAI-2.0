# test_db.py

import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    user="admin",
    password="admin123",
    database="trustnetai"
)

print("CONNECTED")