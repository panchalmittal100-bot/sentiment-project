
Start Frontend:
python -m streamlit run frontend/app.py
# Sentiment Analysis API

## Overview
This project is a machine learning based sentiment analysis system deployed using FastAPI.

## Live URL
https://sentiment-project-0q53.onrender.com

## Features
- Predicts sentiment (Positive/Negative)
- FastAPI backend
- Deployed on Render
- Tested using Swagger UI

## API Endpoints

### GET /
Returns API status

### POST /predict
Input:
{
  "text": "This is amazing"
}

Output:
{
  "prediction": "Positive"
}

## Technologies Used
- Python
- FastAPI
- Scikit-learn
- Render

## How to Run Locally
pip install -r requirements.txt
uvicorn app.main:app --reload