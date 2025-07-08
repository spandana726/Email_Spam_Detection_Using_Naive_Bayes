import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from scipy.sparse import hstack, csr_matrix
import pickle
from utils import clean_text, extract_urls, extract_phone_numbers

df = pd.read_csv("data/enron_spam_data_enriched.csv")
df['text'] = df['Subject'].fillna('') + ' ' + df['Message'].fillna('')
df['cleaned'] = df['text'].apply(clean_text)

vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df['cleaned'])

df['num_links'] = df['text'].apply(lambda x: len(extract_urls(str(x))))
df['num_phones'] = df['text'].apply(lambda x: len(extract_phone_numbers(str(x))))
X_extra = df[['num_links', 'num_phones']].values
X_all = hstack([X, csr_matrix(X_extra)])

y = df['Spam/Ham'].map({'spam': 1, 'ham': 0})
X_train, X_test, y_train, y_test = train_test_split(X_all, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))

with open("models/spam_classifier.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)