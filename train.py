import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

# Ensure directories exist
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)

# 1. Load data (from the placeholder .csv)
print("Loading data from data/reviews.csv...")
df = pd.read_csv("data/reviews.csv")

if df.empty:
    print("data/reviews.csv is empty. Training skipped.")
    print("Please add sample data (e.g., 'text,label') to train the model.")
else:
    # 2. Prepare data and train model
    print("Training tiny classifier...")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['text'])
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 3. Save model artifact
    model_path = "models/model.pkl"
    joblib.dump(model, model_path)
    
    print(f"Model trained and saved to {model_path}")
    
    # 4. (Homework) Generate hashes for data/reviews.csv and models/model.pkl
    print("\nNext steps (for Meeting 3):")
    print("1. Generate the SHA-256 hash for data/reviews.csv")
    print("2. Generate the SHA-256 hash for models/model.pkl")
    print("3. Complete the templates/MODEL_CARD.md")
    print("4. Complete the templates/MBOM.yaml [cite: 144, 161]")