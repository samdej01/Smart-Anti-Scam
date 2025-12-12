# src/model.py
import os
import sys
import joblib

# نجبر PyInstaller يضم الوحدات المستخدمة في الـ pickle
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer  # مهم حتى لو ما استخدمناه مباشرة

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODELS_DIR = os.path.join(BASE_DIR, "models")

TFIDF_PATH = os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl")
MODEL_PATH = os.path.join(MODELS_DIR, "sms_spam_model.pkl")

if not os.path.exists(TFIDF_PATH) or not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model files not found in: {MODELS_DIR}")

tfidf_vectorizer = joblib.load(TFIDF_PATH)
sms_model = joblib.load(MODEL_PATH)


def predict_message(text: str):
    vec = tfidf_vectorizer.transform([text])
    proba_all = sms_model.predict_proba(vec)[0]
    label = sms_model.predict(vec)[0]
    confidence = float(proba_all.max())
    risk = "safe" if label == "ham" else "suspicious"
    return {"label": label, "risk": risk, "confidence": confidence}
