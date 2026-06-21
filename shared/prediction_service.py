from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

print("BASE_DIR =", BASE_DIR)

MODEL_PATH = BASE_DIR / "trustnetai-bert"

print("MODEL_PATH =", MODEL_PATH)
print("EXISTS =", MODEL_PATH.exists())

tokenizer = AutoTokenizer.from_pretrained(str(MODEL_PATH))
model = AutoModelForSequenceClassification.from_pretrained(str(MODEL_PATH))

model.eval()

LABELS = {
    0: "REAL",
    1: "FAKE"
}


def predict_news(text: str):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)

    confidence = torch.max(probs).item()

    prediction = torch.argmax(probs).item()

    return {
        "prediction": LABELS[prediction],
        "confidence": round(confidence, 4)
    }