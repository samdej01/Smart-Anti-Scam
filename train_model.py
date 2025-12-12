# src/train_model.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

def main():
    # Path to dataset
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "SMSSpamCollection.xlsx")
    df = pd.read_excel(data_path, header=None)
    df.columns = ["label", "message"]

    print("Data shape:", df.shape)
    print(df["label"].value_counts())

    df["message"] = df["message"].astype(str)

    # إزالة أي صف فيه رسالة فاضية أو NaN
    df = df[df["message"].str.strip().notna()]
    df = df[df["message"].str.strip() != ""]

    X = df["message"]
    y = df["label"]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # TF-IDF vectorizer
    tfidf = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_features=5000
    )

    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)

    # Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_tfidf, y_train)

    # Evaluation
    y_pred = model.predict(X_test_tfidf)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save model and vectorizer
    models_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")
    os.makedirs(models_dir, exist_ok=True)

    joblib.dump(tfidf, os.path.join(models_dir, "tfidf_vectorizer.pkl"))
    joblib.dump(model, os.path.join(models_dir, "sms_spam_model.pkl"))

    print("Model and vectorizer saved successfully.")

if __name__ == "__main__":
    main()
