
# 📧 Advanced Email Spam Detection System 🛡️

A robust and real-time spam detection system that uses **NLP, ML, phishing URL classifiers, and phone number verification APIs** to analyze email content and **accurately detect spam, phishing links, and fraud phone numbers**.

> Achieves **>95% accuracy** using real-world datasets and integrates APIs like **VirusTotal, PhishTank, and Truecaller**.

---

## Features

- **Spam/Ham Classification** using NLP (TF-IDF + Naive Bayes or DistilBERT)
- 🔗 **Phishing URL Detection** via:
  - ML-trained phishing classifier (`urlset_clean.csv`)
  - [✔️ VirusTotal API](https://virustotal.com)
  - [✔️ PhishTank API](https://phishtank.org/)
- 📞 **Phone Number Detection and Verification** using:
  - Regex-based number extraction
  - [✔️ NumVerify API](https://numverify.com/) or Truecaller API
- **Text Preprocessing**: Lowercasing, stopword removal, tokenization
- **Real-Time Terminal Input Support**
- **Confidence Score** on classification output

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

## Model Overview

| Module             | Description                                 | Dataset                      | Accuracy     |
|--------------------|---------------------------------------------|-------------------------------|--------------|
| Spam Classifier    | TF-IDF + Naive Bayes or DistilBERT          | Enron Spam (enriched)        | ~96.5%       |
| URL Classifier     | Gradient Boosting + URL features            | Phishing/Legit URLs (96k)    | ~95.2%       |
| Phone Checker      | Regex + NumVerify or Truecaller             | Live API Integration          | N/A          |

---

## 1st Example Email (Ham)
```
Dear Spandana Gunaganti,

We are pleased to inform you that you have been shortlisted for the Software Engineer role at Infosys.  
Your application has successfully passed the initial screening.

📅 Interview Date: Monday, July 15, 2025  
🕐 Time: 11:00 AM IST  
📍 Mode: Virtual – Microsoft Teams

🔗 Joining Link (will be active 10 mins before session):  
https://teams.microsoft.com/l/meetup-join/infosys/candidate/July15

Please ensure you are in a quiet location with a stable internet connection.  
Also, keep your resume, government ID proof, and academic transcripts handy during the interview.

For any assistance, feel free to contact us at hr@infosys.com or 📞 1800-123-4567.

We look forward to meeting you.

Warm Regards,  
Recruitment Team  
Infosys Ltd.

💡 Output:
```
🔎 Result: Ham  
📈 Confidence: 97.25%
```

## 2nd Example Email (Spam)
```
Hello Spandana,

Your Apple ID was used to purchase a new iPhone 15 Pro Max – 256GB for ₹87,999 on July 9, 2025.  
Device: iPhone 15 Pro Max  
Location: Indore, India  
IP Address: 182.77.120.53

If you did not authorize this transaction, you must secure your account immediately to prevent further charges.

👉 Cancel Transaction: https://apple-secure-login.support-id-verification.com  
(Note: This link expires in 30 minutes)

Failure to verify within the next 30 minutes will result in permanent charge on your card ending in 1823.  
For support, call us at 📞 +91-9898989898.

Apple Support  
apple-support@icloud.com


💡 Output:
```
🔎 Result: Spam  
📈 Confidence: 95.75%
```
**Demo Outputs**
![Screenshot 2025-07-09 004516](https://github.com/user-attachments/assets/a6ccd3f6-31b3-4aa5-a333-fff307b417f0)
![Screenshot 2025-07-09 004245](https://github.com/user-attachments/assets/0b9af67d-e51e-47ae-8752-ed31bd36f8f7)
![Screenshot 2025-07-09 003843](https://github.com/user-attachments/assets/ed16fb97-006d-4b88-a572-f28b28bcb07a)

## How to Run

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

## Datasets Used

| Dataset File                 | Description                                 | Size       |
|-----------------------------|---------------------------------------------|------------|
| `enron_spam_data_enriched.csv` | Emails with Subject, Message, and labels   | ~35,000    |
| `urlset_clean.csv`             | Phishing and legit URLs + labels           | ~96,000    |

> You can find open datasets at:
> - [https://www.kaggle.com/rtatman/enron-spam-dataset](https://www.kaggle.com/rtatman/enron-spam-dataset)
> - [https://www.kaggle.com/datasets/sid321axn/phishing-site-url-dataset](https://www.kaggle.com/datasets/sid321axn/phishing-site-url-dataset)

---

## APIs Used

| API           | Purpose                        | Link                                  |
|---------------|--------------------------------|---------------------------------------|
| VirusTotal    | Check real-time domain threat  | https://www.virustotal.com            |
| PhishTank     | Known phishing domain scanner  | https://www.phishtank.com             |
| NumVerify     | Phone validation + location    | https://numverify.com                 |
| Truecaller    | Caller name & spam check       | https://www.truecaller.com/developer  |

---

## Future Improvements

- Web dashboard (Streamlit or Flask frontend)
- Email inbox scanning support (IMAP integration)
- BERT-based spam + URL joint models
- Real-time threat feed integration

## Acknowledgements

- Enron Email Dataset
- VirusTotal & PhishTank APIs
- NumVerify/Truecaller API
- scikit-learn, pandas, nltk, requests

---

## 🔗 Connect

Built with [Gunaganti Spandana]  
