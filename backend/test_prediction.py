from shared.prediction_service import predict_news
texts = [
    "Scientists discover new renewable energy source",
    "Celebrity claims moon landing was staged",
    "Aliens are secretly controlling world governments",
    "Government launches new healthcare initiative"
]

for text in texts:
    result = predict_news(text)
    print(text)
    print(result)
    print()