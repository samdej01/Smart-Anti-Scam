# 🛡️ Smart Anti-Scam
### Web-Based SMS Scam Detection Using Machine Learning (NLP)

---

## 📌 Project Overview

Smart Anti-Scam is a web-based machine learning application designed to detect and classify SMS messages as **scam** or **legitimate (ham)**. The system analyzes user-provided text in real time using a trained machine learning model.

The application follows a simple web-based architecture consisting of:
- A Flask backend API for prediction and inference
- A trained machine learning model for SMS classification
- A lightweight HTML-based web interface for user interaction

This project is intended for academic and practical demonstration purposes in applied machine learning, natural language processing (NLP), and scam prevention.

---

## 🌐 Live Demo

🔗 **Live Web Application:**  
*(https://smart-anti-scam.onrender.com)*

---

## 🧠 Machine Learning & NLP Approach

This project applies **traditional Natural Language Processing (NLP)** techniques combined with supervised machine learning.

- Text preprocessing and feature extraction using **TF-IDF vectorization**
- Statistical representation of SMS text (bag-of-words approach)
- Supervised binary classification
- Classification labels: **Scam** / **Not Scam (Ham)**
- Model inference performed in real time using pre-trained components

The trained model and vectorizer are persisted and reused for efficient prediction.

---

## 🛠️ Technology Stack

### Backend & Machine Learning
- Python
- Flask
- Scikit-learn
- TF-IDF Vectorization (NLP)
- Logistic Regression
- Pickle (model persistence)

### Frontend
- HTML
- CSS
- JavaScript

### Dataset
- SMS Spam Collection Dataset

---

## 📁 Project Structure

Smart-Anti-Scam/
│
├── Code/
│ ├── api.py # Flask API for predictions
│ ├── model.py # Model loading and prediction logic
│ └── train_model.py # Optional model training script
│
├── Data/
│ └── SMSSpamCollection.xlsx
│
├── models/
│ ├── sms_spam_model.pkl
│ └── tfidf_vectorizer.pkl
│
├── templates/
│ └── index.html # Web interface
│
├── requirements.txt
└── README.md

---

## 🚀 Running the Project Locally

### 1️⃣ Install Dependencies

Ensure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 2️⃣ (Optional) Train the Machine Learning Model

This step is only required if you want to retrain the model.

```bash
python Code/train_model.py
```

This will generate:
sms_spam_model.pkl
tfidf_vectorizer.pkl

### 3️⃣ Start the Flask Web Server

```bash
python Code/api.py
```

The application will run at:

```bash
http://127.0.0.1:5001/
```

### 4️⃣ Use the Web Application


Open a web browser


Navigate to http://127.0.0.1:5001/


Enter an SMS message


Receive a real-time scam classification result



🎯 Key Features


Real-time SMS scam detection


NLP-based text analysis using TF-IDF


Simple and user-friendly web interface


Reusable trained machine learning model


Clear separation between ML logic and web layer


Lightweight and deployment-ready structure



📌 Notes


This project is web-based only


No desktop or executable application is included


Model files are stored locally for inference efficiency


Designed for educational, academic, and internship submissions

💙
