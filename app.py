import uvicorn
import joblib
from sales_prediction.config.config import MODEL_PATH
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sales_prediction.predict import predict

app = FastAPI(
    title="Sales Prediction API",
    description="API to predict sales using a linear regression model",
    version="0.1",
)

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SalesPredictionRequest(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

class SalesPredictionResponse(BaseModel):
    Sales: float

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Sales Prediction API!"}

@app.post("/predict", response_model=SalesPredictionResponse)
async def predict_endpoint(data: SalesPredictionRequest):
    X = [[data.TV, data.Radio, data.Newspaper]]
    prediction = predict(X)
    return {"Sales": prediction}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port="8000")