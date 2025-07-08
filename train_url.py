import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import pickle
from utils import extract_url_features

df = pd.read_csv("data/urlset_clean.csv", encoding='ISO-8859-1')

df.columns = df.columns.str.strip().str.lower()

if 'domain' not in df.columns or 'label' not in df.columns:
    raise KeyError("CSV must contain 'domain' and 'label' columns.")

df = df.dropna(subset=['domain'])

X = df['domain'].apply(extract_url_features).tolist()
y = df['label']

model = GradientBoostingClassifier()
model.fit(X, y)

print(" URL Model Trained")

with open("models/url_clf.pkl", "wb") as f:
    pickle.dump(model, f)
