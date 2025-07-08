
# 📧 Advanced Email Spam Detection System 🛡️

A robust and real-time spam detection system that uses **NLP, ML, phishing URL classifiers, and phone number verification APIs** to analyze email content and **accurately detect spam, phishing links, and fraud phone numbers**.

> Achieves **>95% accuracy** using real-world datasets and integrates APIs like **VirusTotal, PhishTank, and Truecaller**.

---

## 🚀 Features

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
├── data/
│   ├── enron_spam_data_enriched.csv
│   └── urlset_clean.csv
├── models/
│   ├── spam_classifier.pkl
│   └── url_clf.pkl
├── utils.py
├── apis.py
├── train_spam.py
├── train_url.py
├── main.py
├── requirements.txt
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

## 📧 Example 1 (Ham)
```
Dear Spandana Gunaganti,

We are pleased to inform you that you have been shortlisted for the Software Engineer role at Infosys.  
Your application has successfully passed the initial screening.

📅 Interview Date: Monday, July 15, 2025  
🕐 Time: 11:00 AM IST  
📍 Mode: Virtual – Microsoft Teams

🔗 Joining Link: https://teams.microsoft.com/l/meetup-join/infosys/candidate/July15

For any assistance, contact us at hr@infosys.com or 📞 1800-123-4567.

Warm Regards,  
Recruitment Team  
Infosys Ltd.
```

💡 **Output:**
```
🔎 Result: Ham  
📈 Confidence: 97.25%
```

---

## ⚠️ Example 2 (Spam)
```
Hello Spandana,

Your Apple ID was used to purchase a new iPhone 15 Pro Max – 256GB for ₹87,999 on July 9, 2025.  
Location: Indore, India  
IP Address: 182.77.120.53

👉 Cancel Transaction: https://apple-secure-login.support-id-verification.com  
Link expires in 30 minutes.

Call us at 📞 +91-9898989898.

Apple Support  
apple-support@icloud.com
```

💡 **Output:**
```
🔎 Result: Spam  
📈 Confidence: 95.75%
```

---

## 🖼️ Demo Outputs

![Screenshot 1](https://github.com/user-attachments/assets/a6ccd3f6-31b3-4aa5-a333-fff307b417f0)
![Screenshot 2](https://github.com/user-attachments/assets/0b9af67d-e51e-47ae-8752-ed31bd36f8f7)
![Screenshot 3](https://github.com/user-attachments/assets/ed16fb97-006d-4b88-a572-f28b28bcb07a)

---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/email_spam_detection.git
cd email_spam_detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Keys
Edit `main.py`:
```python
VT_API_KEY = 'your_virustotal_api_key'
TRUECALLER_API_KEY = 'your_numverify_api_key'
```

### 4. Train models
```bash
python train_spam.py
python train_url.py
```

### 5. Run the system
```bash
python main.py
```

---

## 📊 Datasets Used

| Dataset File                 | Description                                 | Size       |
|-----------------------------|---------------------------------------------|------------|
| enron_spam_data_enriched.csv | Emails with Subject, Message, and labels   | ~35,000    |
| urlset_clean.csv             | Phishing and legit URLs + labels           | ~96,000    |

> Sources:  
> - [Enron Spam Dataset](https://www.kaggle.com/rtatman/enron-spam-dataset)  
> - [Phishing URL Dataset](https://www.kaggle.com/datasets/sid321axn/phishing-site-url-dataset)

---

## 🌐 APIs Used

| API           | Purpose                        | Link                                  |
|---------------|--------------------------------|---------------------------------------|
| VirusTotal    | Check real-time domain threat  | https://www.virustotal.com            |
| PhishTank     | Known phishing domain scanner  | https://www.phishtank.com             |
| NumVerify     | Phone validation + location    | https://numverify.com                 |
| Truecaller    | Caller name & spam check       | https://www.truecaller.com/developer  |

---

## 🚧 Future Improvements

- Web dashboard (Streamlit or Flask)
- Email inbox scanning (IMAP)
- BERT-based spam + URL joint models
- Real-time threat feed integration

---

## 🙌 Acknowledgements

- Enron Dataset  
- VirusTotal & PhishTank  
- NumVerify & Truecaller APIs  
- scikit-learn, pandas, nltk, requests

---

## 🧑‍💻 Author

Built with ❤️ by **Spandana Gunaganti**
