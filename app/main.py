from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


@app.get("/")
def home():
    return {"message": "Sentiment API is running"}


@app.post("/predict")
def predict(text: str):

    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)

    if prediction[0] == 1:
        result = "Positive"
    else:
        result = "Negative"

    return {"prediction": result}