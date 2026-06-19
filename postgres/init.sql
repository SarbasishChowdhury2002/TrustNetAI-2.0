CREATE TABLE news_analysis (
    id SERIAL PRIMARY KEY,

    news_id VARCHAR(100),

    title TEXT,

    prediction VARCHAR(20),

    confidence FLOAT,

    explanation TEXT,

    blockchain_hash TEXT,

    timestamp TIMESTAMP
);