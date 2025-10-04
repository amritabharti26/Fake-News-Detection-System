import sys
sys.stdout.reconfigure(encoding='utf-8')
# train.py
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import joblib

# Get the current script folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load datasets using absolute paths
true = pd.read_csv(os.path.join(BASE_DIR, "True.csv"))
fake = pd.read_csv(os.path.join(BASE_DIR, "Fake.csv"))

# Add labels
true['label'] = "REAL"
fake['label'] = "FAKE"

# Combine datasets
data = pd.concat([true, fake], axis=0).reset_index(drop=True)

# Split features and labels
X = data['text']
y = data['label']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train SVM
model = svm.LinearSVC()
model.fit(X_train, y_train)

# Print accuracy
print("Accuracy:", model.score(X_test, y_test))

# Save model + vectorizer in same folder
joblib.dump(model, os.path.join(BASE_DIR, "fake_news_model.pkl"))
joblib.dump(vectorizer, os.path.join(BASE_DIR, "vectorizer.pkl"))

print("✅ Model and vectorizer saved in backend folder!")

