import re
import nltk
from nltk.corpus import stopwords
from urllib.parse import urlparse
from collections import Counter
import math

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", " link ", text)
    text = re.sub(r"\S+@\S+", " email ", text)
    text = re.sub(r"\+?\d[\d\s().-]{7,}\d", " phone ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\W+", " ", text)
    return " ".join(w for w in text.split() if w not in stop_words)

def extract_urls(text):
    return re.findall(r"http\S+|www\S+", text)

def extract_phone_numbers(text):
    return re.findall(r"\+?\d[\d\s().-]{7,}\d", text)

def shannon_entropy(string):
    counter = Counter(string)
    length = len(string)
    return -sum((count / length) * math.log2(count / length) for count in counter.values() if count)

def extract_url_features(url):
    try:
        parsed = urlparse(url if url.startswith("http") else "http://" + url)
        hostname = parsed.netloc or parsed.path
        full = parsed.geturl()
        return [
            len(full),
            shannon_entropy(full),
            1 if re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$", hostname) else 0,
            hostname.count('.'),
            full.count('-'),
            full.count('@'),
            full.count('/'),
            1 if 'https' in full else 0,
            1 if 'login' in full.lower() else 0,
            1 if any(s in hostname.lower() for s in ['bit.ly', 'tinyurl', 't.co', 'goo.gl']) else 0
        ]
    except:
        return [0]*10