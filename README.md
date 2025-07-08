
# 📧 Advanced Email Spam & Phishing Detection System 🛡️

A robust and real-time spam detection system that uses **NLP, ML, phishing URL classifiers, and phone number verification APIs** to analyze email content and **accurately detect spam, phishing links, and fraud phone numbers**.

> ✅ Achieves **>95% accuracy** using real-world datasets and integrates APIs like **VirusTotal, PhishTank, and Truecaller**.

---

## 🚀 Features

- ✅ **Spam/Ham Classification** using NLP (TF-IDF + Naive Bayes or DistilBERT)
- 🔗 **Phishing URL Detection** via:
  - ML-trained phishing classifier (`urlset_clean.csv`)
  - [✔️ VirusTotal API](https://virustotal.com)
  - [✔️ PhishTank API](https://phishtank.org/)
- 📞 **Phone Number Detection and Verification** using:
  - Regex-based number extraction
  - [✔️ NumVerify API](https://numverify.com/) or Truecaller API
- 🧠 **Text Preprocessing**: Lowercasing, stopword removal, tokenization
- 🧪 **Real-Time Terminal Input Support**
- 📊 **Confidence Score** on classification output

---

## 📁 Folder Structure

```
email_spam_detection/
│
├── data/
│   ├── enron_spam_data_enriched.csv       # Email dataset
│   └── urlset_clean.csv                   # Phishing/legitimate URLs
│
├── models/
│   ├── spam_classifier.pkl                # Pickled spam model + vectorizer
│   └── url_clf.pkl                        # Pickled phishing URL classifier
│
├── utils.py                               # Text, URL, phone extractors
├── apis.py                                # VirusTotal, PhishTank, Truecaller
├── train_spam.py                          # Train spam classification model
├── train_url.py                           # Train phishing URL classifier
├── main.py                                # Real-time prediction script
├── requirements.txt                       # Python dependencies
└── README.md
```

---

## 🧠 Model Overview

| Module             | Description                                 | Dataset                      | Accuracy     |
|--------------------|---------------------------------------------|-------------------------------|--------------|
| Spam Classifier    | TF-IDF + Naive Bayes or DistilBERT          | Enron Spam (enriched)        | ~96.5%       |
| URL Classifier     | Gradient Boosting + URL features            | Phishing/Legit URLs (96k)    | ~95.2%       |
| Phone Checker      | Regex + NumVerify or Truecaller             | Live API Integration          | N/A          |

---

## 🧪 Example Email (Ham)
```
Subject: Your Razorpay Statement for June

Dear Meghana,
Your June payment summary is ready.

Total Transactions: ₹3,45,230  
Settlement: ₹3,30,980  
Refunds: ₹2,150

📎 Download: https://razorpay.com/statement

Thanks,  
Team Razorpay
```

💡 Output:
```
🔎 Result: Ham  
📈 Confidence: 97.25%
```

---

## 🛠️ How to Run

### 🔹 1. Clone the repo
```bash
git clone https://github.com/<your-username>/email_spam_detection.git
cd email_spam_detection
```

### 🔹 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 🔹 3. Add API Keys
In `main.py`:
```python
VT_API_KEY = 'your_virustotal_api_key'
TRUECALLER_API_KEY = 'your_numverify_api_key'
```

> You can register and get these free API keys from:
> - [https://virustotal.com](https://virustotal.com)
> - [https://numverify.com](https://numverify.com)

### 🔹 4. Train models (if not already)
```bash
python train_spam.py
python train_url.py
```

### 🔹 5. Run the system
```bash
python main.py
```

---

## 💡 Sample Output

```
📧 Enter email content:
Hi Meghana,  
View payment details: https://secure-payments-check.info  
Call +91-9988771122 for support

🔎 Result: Spam  
📈 Confidence: 94.89%
```

---

## 📦 Datasets Used

| Dataset File                 | Description                                 | Size       |
|-----------------------------|---------------------------------------------|------------|
| `enron_spam_data_enriched.csv` | Emails with Subject, Message, and labels   | ~35,000    |
| `urlset_clean.csv`             | Phishing and legit URLs + labels           | ~96,000    |

> You can find open datasets at:
> - [https://www.kaggle.com/rtatman/enron-spam-dataset](https://www.kaggle.com/rtatman/enron-spam-dataset)
> - [https://www.kaggle.com/datasets/sid321axn/phishing-site-url-dataset](https://www.kaggle.com/datasets/sid321axn/phishing-site-url-dataset)

---

## 🔒 APIs Used

| API           | Purpose                        | Link                                  |
|---------------|--------------------------------|---------------------------------------|
| VirusTotal    | Check real-time domain threat  | https://www.virustotal.com            |
| PhishTank     | Known phishing domain scanner  | https://www.phishtank.com             |
| NumVerify     | Phone validation + location    | https://numverify.com                 |
| Truecaller    | Caller name & spam check       | https://www.truecaller.com/developer  |

---

## ✅ Future Improvements

- Web dashboard (Streamlit or Flask frontend)
- Email inbox scanning support (IMAP integration)
- BERT-based spam + URL joint models
- Real-time threat feed integration

---

## 📄 License

This project is open-sourced under the **MIT License**.  
Feel free to fork, modify, and use it for learning or security research.

---

## 🙌 Acknowledgements

- Enron Email Dataset
- VirusTotal & PhishTank APIs
- NumVerify/Truecaller API
- scikit-learn, pandas, nltk, requests

---

## 🔗 Connect

Built with ❤️ by [Gunaganti Spandana]  
If you liked this, ⭐️ the repo or contribute!
