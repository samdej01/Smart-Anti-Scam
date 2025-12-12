# src/api.py
import os
from flask import Flask, request, jsonify, render_template
from model import predict_message

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATES_DIR)

@app.route("/", methods=["GET"])
def index():
    # يرجع ملف HTML من templates/index.html
    return render_template("index.html")

@app.route("/predict_sms", methods=["POST"])
def predict_sms():
    data = request.get_json(force=True, silent=True)
    if not data or "message" not in data:
        return jsonify({"error": "Please send JSON with a 'message' field."}), 400

    text = data["message"]
    result = predict_message(text)

    return jsonify({
        "input_message": text,
        "prediction": {
            "label": result["label"],
            "risk": result["risk"],
            "confidence": result["confidence"]
        }
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50001))  
    app.run(host="0.0.0.0", port=port, debug=True)
