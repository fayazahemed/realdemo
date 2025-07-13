from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class InsuranceData(BaseModel):
    Age: int
    Gender: int
    Vehicle_Age: int
    Vehicle_Type: int
    Annual_Premium: float

@app.get("/")
def read_root():
    return {"msg": "Welcome to Insurance Claim Predictor!"}

@app.post("/predict")
def predict(data: InsuranceData):
    input_data = np.array([[data.Age, data.Gender, data.Vehicle_Age, data.Vehicle_Type, data.Annual_Premium]])
    prediction = model.predict(input_data)[0]
    return {"Claim": int(prediction)}

