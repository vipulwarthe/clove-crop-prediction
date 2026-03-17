from fastapi import FastAPI
import numpy as np
from src.models.predict import predict

app = FastAPI(title="Clove Crop Prediction API")

@app.get("/")
def home():
    return {"message": "Clove ML API Running"}

@app.post("/predict")
def get_prediction(data: list):
    arr = np.array(data)
    preds = predict(arr)
    return {"prediction": preds.tolist()}