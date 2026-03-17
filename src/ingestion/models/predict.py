import joblib
import numpy as np
from src.utils.config import Config

def load_model():
    return joblib.load(Config.MODEL_PATH)

def predict(data):
    model = load_model()
    data = np.array(data)
    return model.predict(data)