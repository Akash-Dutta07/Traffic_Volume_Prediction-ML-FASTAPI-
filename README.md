# 🚇 Metro Interstate Traffic Volume Predictor

A **full-stack machine learning application** built with **FastAPI** and **Streamlit** for predicting hourly traffic volume on metropolitan interstate highways.

## 🏗️ **Architecture Overview**

This project demonstrates **multiple deployment strategies** and **API-first development**:

### **FastAPI Backend** (`api.py`)
- ✅ **RESTful API** with automatic OpenAPI documentation
- ✅ **Pydantic models** for data validation
- ✅ **ML model serving** with joblib pipeline
- ✅ **Error handling** and response formatting
- ✅ **CORS support** for frontend integration

### **Streamlit Frontend** (`frontend.py`)
- ✅ **Interactive web interface** with real-time predictions
- ✅ **Dual mode support**: API calls (local) + Direct model loading (cloud)
- ✅ **Responsive design** with sidebar controls
- ✅ **Input validation** and user feedback

## 🚀 **Deployment Options**

### **Option 1: FastAPI + Streamlit (Local Development)**
```bash
# Terminal 1: Start FastAPI server
uvicorn api:app --reload --host 127.0.0.1 --port 8000

# Terminal 2: Start Streamlit app (with API integration)
streamlit run frontend_api.py
```

### **Option 2: Standalone Streamlit (Cloud Deployment)**
```bash
# Single command deployment
streamlit run frontend.py
```
**🌐 Live Demo:** [Streamlit Cloud Deployment](https://your-app-url.streamlit.app)

## 🛠️ **FastAPI Features Demonstrated**

### **API Endpoints**
- `GET /` - Health check and API information
- `POST /predict` - Traffic volume prediction endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

### **Technical Implementation**
```python
# Pydantic model for request validation
class TrafficData(BaseModel):
    holiday: str = 'None'
    temp: float = 288.28
    rain_1h: float = 0.0
    # ... more fields

# FastAPI endpoint with error handling
@app.post("/predict")
def predict_traffic_volume(data: TrafficData):
    # ML prediction logic
    return {"predicted_traffic_volume": predicted_volume}
```

## 📊 **Machine Learning Pipeline**

- **Data Processing**: Feature engineering, encoding, scaling
- **Model**: Trained on Metro Interstate Traffic Volume dataset
- **Serialization**: Joblib pipeline for consistent preprocessing + prediction
- **Validation**: Pydantic schemas ensure data quality

## 🔧 **Local Development Setup**

### **Prerequisites**
```bash
python 3.8+
pip or conda
```

### **Installation**
```bash
# Clone repository
git clone https://github.com/Akash-Dutta07/Traffic_Volume_Prediction-ML-FASTAPI-.git
cd Traffic_Volume_Prediction-ML-FASTAPI-

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### **Run FastAPI Server**
```bash
uvicorn api:app --reload
```
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

### **Run Streamlit App**
```bash
streamlit run frontend.py
```

## 📋 **Project Structure**
```
├── api.py                     # FastAPI backend server
├── frontend.py                # Streamlit frontend (cloud-ready)
├── frontend_api.py           # Streamlit frontend (API integration)
├── notebook.ipynb            # ML model development
├── traffic_model_pipeline.joblib  # Trained model
├── requirements.txt          # Dependencies
├── pyproject.toml           # Project configuration
└── README.md                # Documentation
```

## 🎯 **Skills Demonstrated**

### **Backend Development**
- ✅ **FastAPI** framework mastery
- ✅ **RESTful API** design principles
- ✅ **Data validation** with Pydantic
- ✅ **Error handling** and logging
- ✅ **API documentation** (OpenAPI/Swagger)

### **Frontend Development**
- ✅ **Streamlit** for rapid prototyping
- ✅ **Interactive UI/UX** design
- ✅ **Real-time data visualization**
- ✅ **Responsive web interfaces**

### **Machine Learning**
- ✅ **End-to-end ML pipeline**
- ✅ **Model serialization** and deployment
- ✅ **Feature engineering**
- ✅ **Production-ready** model serving

### **DevOps & Deployment**
- ✅ **Multiple deployment strategies**
- ✅ **Cloud deployment** (Streamlit Cloud)
- ✅ **Local development** environment
- ✅ **Version control** with Git

## 🧪 **API Testing**

### **Using curl**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "holiday": "None",
       "temp": 295.15,
       "clouds_all": 75,
       "weather_main": "Clouds",
       "hour": 17,
       "day_of_week": 0,
       "month": 6,
       "is_rush_hour": 1
     }'
```

### **Expected Response**
```json
{
  "predicted_traffic_volume": 4521
}
```

## 📈 **Future Enhancements**

- [ ] **Docker containerization**
- [ ] **Database integration** for prediction logging
- [ ] **Authentication & authorization**
- [ ] **Rate limiting** and caching
- [ ] **Model versioning** and A/B testing
- [ ] **Monitoring & observability**

## 📞 **Contact**

**Akash Dutta**
- GitHub: [@Akash-Dutta07](https://github.com/Akash-Dutta07)
- LinkedIn: [Your LinkedIn Profile]

---

*This project demonstrates full-stack ML development capabilities with modern Python frameworks and deployment strategies.*