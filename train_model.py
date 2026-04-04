import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

data = {
    "text": [
        "I love this product",
        "This is amazing",
        "Very good service",
        "I am very happy",
        "This is bad",
        "I hate this",
        "Very poor quality",
        "This is terrible"
    ],
    "label": [1,1,1,1,0,0,0,0]
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

y = df["label"]

# Train model
model = LogisticRegression()
model.fit(X,y)

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Save 
joblib.dump(model,"model/model.pkl")
joblib.dump(vectorizer,"model/vectorizer.pkl")

print("Model trained and saved successfully!")