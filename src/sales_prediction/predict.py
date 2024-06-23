import joblib
from sales_prediction.config.config import MODEL_PATH

def predict(data):
    model = joblib.load(MODEL_PATH / "model.pkl")
    return model.predict(data)