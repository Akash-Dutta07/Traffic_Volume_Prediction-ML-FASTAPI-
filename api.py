from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from typing import Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Metro Interstate Traffic Volume Prediction API",
    description="A machine learning API for predicting hourly traffic volume on metropolitan interstate highways.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
try:
    model_pipeline = joblib.load('traffic_model_pipeline.joblib')
    print("Model pipeline loaded successfully.")
except FileNotFoundError:
    print("Error: Model file 'traffic_model_pipeline.joblib' not found.")
    print("Please run the Jupyter Notebook first to train and save the model.")
    model_pipeline = None


class TrafficData(BaseModel):
    holiday: str = Field(default='None', description="Holiday name or 'None'")
    temp: float = Field(default=288.28, description="Temperature in Kelvin", ge=200, le=350)
    rain_1h: float = Field(default=0.0, description="Rain volume in last hour (mm)", ge=0)
    snow_1h: float = Field(default=0.0, description="Snow volume in last hour (mm)", ge=0)
    clouds_all: int = Field(default=40, description="Cloud cover percentage", ge=0, le=100)
    weather_main: str = Field(default='Clouds', description="Main weather condition")
    hour: int = Field(default=9, description="Hour of day (0-23)", ge=0, le=23)
    day_of_week: int = Field(default=1, description="Day of week (0=Monday, 6=Sunday)", ge=0, le=6)
    month: int = Field(default=10, description="Month (1-12)", ge=1, le=12)
    is_rush_hour: int = Field(default=1, description="Rush hour flag (0 or 1)", ge=0, le=1)

    class Config:
        schema_extra = {
            "example": {
                "holiday": "None",
                "temp": 295.15,
                "rain_1h": 0.0,
                "snow_1h": 0.0,
                "clouds_all": 75,
                "weather_main": "Clouds",
                "hour": 17,
                "day_of_week": 0,
                "month": 6,
                "is_rush_hour": 1
            }
        }

class PredictionResponse(BaseModel):
    predicted_traffic_volume: int = Field(description="Predicted traffic volume (vehicles/hour)")
    model_version: str = Field(description="Model version used for prediction")
    
class ErrorResponse(BaseModel):
    error: str = Field(description="Error message")
    detail: str = Field(description="Detailed error information")


@app.get("/")
def read_root() -> Dict[str, Any]:
    """
    Health check endpoint - returns API status and information.
    """
    return {
        "message": "Metro Interstate Traffic Volume Prediction API",
        "status": "running",
        "model_loaded": model_pipeline is not None,
        "version": "1.0.0",
        "docs_url": "/docs",
        "endpoints": {
            "predict": "POST /predict - Make traffic volume prediction",
            "health": "GET / - API health check",
            "docs": "GET /docs - Interactive API documentation"
        }
    }

@app.get("/health")
def health_check() -> Dict[str, Any]:
    """
    Detailed health check endpoint.
    """
    return {
        "status": "healthy" if model_pipeline else "unhealthy",
        "model_loaded": model_pipeline is not None,
        "timestamp": pd.Timestamp.now().isoformat()
    }

@app.post("/predict", response_model=PredictionResponse, responses={
    400: {"model": ErrorResponse, "description": "Bad Request"},
    500: {"model": ErrorResponse, "description": "Internal Server Error"}
})
def predict_traffic_volume(data: TrafficData) -> PredictionResponse:
    """
    Predict traffic volume based on input features.
    
    This endpoint accepts traffic-related parameters and returns a prediction
    of the expected hourly traffic volume using a trained machine learning model.
    
    - **holiday**: Holiday name or 'None' if not a holiday
    - **temp**: Temperature in Kelvin (typically 200-350K)
    - **rain_1h**: Rainfall in the last hour (mm)
    - **snow_1h**: Snowfall in the last hour (mm) 
    - **clouds_all**: Cloud cover percentage (0-100%)
    - **weather_main**: Main weather condition
    - **hour**: Hour of the day (0-23)
    - **day_of_week**: Day of week (0=Monday, 6=Sunday)
    - **month**: Month of the year (1-12)
    - **is_rush_hour**: Whether it's rush hour (0 or 1)
    """
    if not model_pipeline:
        logger.error("Model not loaded")
        raise HTTPException(
            status_code=500,
            detail="Model not loaded. Please check API server logs."
        )
    
    try:
        # Log the prediction request
        logger.info(f"Prediction request received: {data.model_dump()}")
        
        # Convert to DataFrame for model prediction
        input_df = pd.DataFrame([data.model_dump()])
        
        # Make prediction
        prediction = model_pipeline.predict(input_df)
        predicted_volume = int(prediction[0])
        
        # Log successful prediction
        logger.info(f"Prediction successful: {predicted_volume}")
        
        return PredictionResponse(
            predicted_traffic_volume=predicted_volume,
            model_version="1.0.0"
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"Invalid input data: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during prediction: {str(e)}"
        )