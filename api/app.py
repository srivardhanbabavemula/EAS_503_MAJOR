from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# Load model
model = joblib.load("models/random_forest_optuna.pkl")

class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: InputData):
    X = np.array(data.features).reshape(1, -1)

    prediction = int(model.predict(X)[0])
    probability = float(model.predict_proba(X)[0][1])

    return {
        "prediction": prediction,
        "probability": probability
    }
