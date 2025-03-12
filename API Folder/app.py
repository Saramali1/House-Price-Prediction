import logging
from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from pydantic import BaseModel

logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    model = joblib.load("house_price_model.pkl")

    try:
        scaler = joblib.load("scaler.pkl")
    except FileNotFoundError:
        logging.warning("Scaler file not found, proceeding without scaling.")
        scaler = None

    logging.info("Model and scaler loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model or scaler: {e}")
    raise RuntimeError("Failed to load model or scaler.")

app = FastAPI()

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def home():
    return {"message": "California House Price Prediction API"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    try:
        input_data = np.array([[features.MedInc, features.HouseAge, features.AveRooms,
                                features.AveBedrms, features.Population, features.AveOccup,
                                features.Latitude, features.Longitude]])

        if scaler:
            input_data = scaler.transform(input_data)
        
        prediction = model.predict(input_data)
        predicted_price = round(prediction[0] * 100000, 2)

        logging.info(f"Prediction successful: ${predicted_price}")
        return {"predicted_price": f"${predicted_price}"}

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail="Invalid input values.")

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")
