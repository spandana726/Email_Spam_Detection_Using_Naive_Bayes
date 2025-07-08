from flask import Flask, request, jsonify
from flask_cors import CORS 
import re
import pickle
import numpy as np
from scipy.sparse import hstack
from utils import clean_text, extract_urls, extract_phone_numbers
from apis import phishtank_check, virustotal_check, truecaller_check

VT_API_KEY = '4bbea0e0d16edb04842aff81755237df1c7645fab63b4e7d0e7699fec1f29f0d'
TRUECALLER_API_KEY = '51ed6a19bcea8c3f9f87ede40c0062de'

with open("models/spam_classifier.pkl", "rb") as f:
    vectorizer, spam_model = pickle.load(f)

with open("models/url_clf.pkl", "rb") as f:
    url_model = pickle.load(f)

app = Flask(__name__)
CORS(app) 

@app.route("/", methods=["GET"])
def home():
    return "✅ Spam & Phishing Detection API is running!", 200

@app.route("/favicon.ico")
def favicon():
    return "", 204

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    email = data.get("message", "")

    if not email:
        return jsonify({"error": "Empty message"}), 400

    urls = extract_urls(email)
    phones = extract_phone_numbers(email)

    vec = vectorizer.transform([clean_text(email)])
    extras = np.array([[len(urls), len(phones)]])
    full_input = hstack([vec, extras])

    spam_probs = spam_model.predict_proba(full_input)[0]
    spam_label = 1 if spam_probs[1] > 0.7 else 0
    confidence = round(spam_probs[spam_label] * 100, 2)

    result = "Spam" if spam_label == 1 else "Ham"

    return jsonify({
        "result": result,
        "confidence": confidence,
        "url_count": len(urls),
        "phone_count": len(phones)
    })

if __name__ == "__main__":
    app.run(debug=True)
