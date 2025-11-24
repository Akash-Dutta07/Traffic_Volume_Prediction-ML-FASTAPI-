# 🚇 Metro Interstate Traffic Volume Predictor

> **A production-ready machine learning application** built with **FastAPI** and **Streamlit** that predicts hourly traffic volume on metropolitan interstate highways using advanced ML techniques.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mozuwedms7bay8bmm2s4m7.streamlit.app/)

## 🎯 **Live Demo**

**🌐 [Try the Live Application](https://mozuwedms7bay8bmm2s4m7.streamlit.app/)**  
*No installation required - test the model instantly!*

---

## 🏗️ **Project Architecture**

This project showcases **professional full-stack ML development** with dual deployment strategies:

### 🔧 **FastAPI Backend** (`api.py`)
- ✅ **RESTful API** with comprehensive OpenAPI documentation
- ✅ **Pydantic models** for robust data validation & type safety
- ✅ **Production-grade error handling** with proper HTTP status codes
- ✅ **ML model serving** with optimized joblib pipeline
- ✅ **CORS middleware** for seamless frontend integration
- ✅ **Structured logging** for monitoring and debugging

### 🎨 **Streamlit Frontend** (`frontend.py` & `frontend_api.py`)
- ✅ **Interactive web interface** with intuitive user controls
- ✅ **Dual deployment modes**: API integration (local) + Direct model (cloud)
- ✅ **Real-time predictions** with instant feedback
- ✅ **Responsive design** with professional UI/UX
- ✅ **Input validation** and comprehensive error handling

## 🚀 **Quick Start Options**

### **Option 1: 🌐 Instant Demo (Recommended)**
**[Click here to use the live application](https://mozuwedms7bay8bmm2s4m7.streamlit.app/)**
- No setup required
- Immediate model testing
- Full feature access

### **Option 2: 💻 Local Development (Full Experience)**
```bash
# Clone the repository
git clone https://github.com/Akash-Dutta07/Traffic_Volume_Prediction-ML-FASTAPI-.git
cd Traffic_Volume_Prediction-ML-FASTAPI-

# Install dependencies
pip install -r requirements.txt

# Terminal 1: Launch FastAPI server
uvicorn api:app --reload

# Terminal 2: Launch Streamlit with API integration
streamlit run frontend_api.py
```

**Local URLs:**
- 🚀 **API Documentation:** http://localhost:8000/docs
- 📊 **Streamlit App:** http://localhost:8501
- 🔍 **Alternative API Docs:** http://localhost:8000/redoc

## ⚡ **Key Features**

### 🤖 **Machine Learning**
- **Advanced pipeline** with preprocessing, feature engineering, and model prediction
- **Robust model** trained on real Metro Interstate Traffic Volume dataset
- **Production serialization** using joblib for consistent performance
- **Real-time predictions** with sub-second response times

### 🛠️ **FastAPI Backend**
- **Professional API design** following RESTful principles
- **Comprehensive validation** with Pydantic field constraints
- **Auto-generated documentation** (Swagger UI + ReDoc)
- **Production error handling** with structured logging
- **CORS support** for frontend integration

### 🎨 **Streamlit Frontend**
- **Intuitive interface** with sidebar controls and real-time feedback
- **Professional UI/UX** with organized layout and visual indicators
- **Input validation** with helpful error messages
- **Responsive design** that works on desktop and mobile

### 📡 **API Endpoints**
```http
GET  /           # API health check and information
POST /predict    # Traffic volume prediction
GET  /health     # Detailed health status  
GET  /docs       # Interactive API documentation
GET  /redoc      # Alternative documentation
```

## 🧠 **Model & Dataset**

### **Dataset Information**
- **Source**: Metro Interstate Traffic Volume Dataset
- **Features**: Weather conditions, holidays, time factors, and traffic patterns
- **Target**: Hourly traffic volume (vehicles per hour)
- **Size**: Comprehensive dataset with seasonal and temporal variations

### **Model Pipeline**
- **Preprocessing**: Feature encoding, scaling, and engineering
- **Algorithm**: Trained machine learning model optimized for traffic prediction
- **Validation**: Cross-validated for robust performance
- **Deployment**: Serialized with joblib for production consistency

## 💻 **Technical Implementation**

### **Pydantic Model Example**
```python
class TrafficData(BaseModel):
    holiday: str = Field(default='None', description="Holiday name")
    temp: float = Field(ge=200, le=350, description="Temperature in Kelvin")
    weather_main: str = Field(description="Main weather condition")
    hour: int = Field(ge=0, le=23, description="Hour of day")
    # ... additional validated fields
```

### **FastAPI Endpoint**
```python
@app.post("/predict", response_model=PredictionResponse)
async def predict_traffic_volume(data: TrafficData):
    # Input validation, model prediction, error handling
    return {"predicted_traffic_volume": prediction}
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

## 🎯 **Technologies & Skills Showcased**

<table>
<tr>
<td>

**🔧 Backend Development**
- ✅ **FastAPI** - Modern Python web framework
- ✅ **Pydantic** - Data validation & serialization
- ✅ **RESTful APIs** - Professional API design
- ✅ **OpenAPI/Swagger** - Auto-documentation
- ✅ **Error handling** - Production-grade responses
- ✅ **CORS & Middleware** - Web integration

</td>
<td>

**🎨 Frontend Development** 
- ✅ **Streamlit** - Rapid web app development
- ✅ **Interactive UI/UX** - User-friendly interfaces
- ✅ **Real-time updates** - Dynamic content
- ✅ **Responsive design** - Cross-platform compatibility
- ✅ **State management** - Efficient app flow

</td>
</tr>
<tr>
<td>

**🤖 Machine Learning**
- ✅ **Scikit-learn** - ML model development
- ✅ **Feature engineering** - Data preprocessing
- ✅ **Model serialization** - Production deployment
- ✅ **Pipeline design** - End-to-end workflows
- ✅ **Prediction APIs** - ML model serving

</td>
<td>

**🚀 DevOps & Deployment**
- ✅ **Cloud deployment** - Streamlit Cloud
- ✅ **Local development** - Full-stack setup
- ✅ **Version control** - Git & GitHub
- ✅ **Documentation** - Professional README
- ✅ **Multiple environments** - Dev/Prod strategies

</td>
</tr>
</table>

## 🧪 **Testing the API**

### **Interactive Testing**
1. Start the FastAPI server: `uvicorn api:app --reload`  
2. Visit **http://localhost:8000/docs** for interactive API testing
3. Use the built-in Swagger UI to test endpoints with sample data

### **cURL Example**
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

### **Sample Response**
```json
{
  "predicted_traffic_volume": 4521,
  "model_version": "1.0.0"
}
```

## 📁 **Project Structure**

```
Traffic_Volume_Prediction-ML-FASTAPI-/
├── 📊 notebook.ipynb              # Model development & training
├── 🔧 api.py                     # FastAPI backend server  
├── 🎨 frontend.py                # Streamlit app (cloud deployment)
├── 🎨 frontend_api.py            # Streamlit app (API integration)
├── 🤖 traffic_model_pipeline.joblib  # Trained ML model
├── 📋 requirements.txt           # Python dependencies
├── ⚙️ pyproject.toml            # Project configuration
├── 📈 Metro_Interstate_Traffic_Volume.csv  # Dataset
├── 📝 README.md                 # Project documentation
└── 📄 LICENSE                   # License information
```

## 🚀 **Why This Project Stands Out**

### **🎯 For Recruiters & Managers**
- **Instant demo** via live Streamlit link - no technical setup required
- **Clear business value** - practical traffic prediction application
- **Professional presentation** with comprehensive documentation

### **👨‍💻 For Technical Interviewers**
- **Full-stack architecture** demonstrating API + frontend integration
- **Production-ready code** with proper error handling and validation
- **Multiple deployment strategies** showing DevOps understanding
- **Clean, documented codebase** following best practices

### **🏆 Professional Development Practices**
- ✅ **API-first design** with comprehensive documentation
- ✅ **Type safety** with Pydantic models and Python type hints
- ✅ **Error handling** with proper HTTP status codes
- ✅ **Separation of concerns** - modular, maintainable code
- ✅ **Production deployment** - real working application

## 🤝 **Contributing**

Interested in contributing? Great! Here's how:

1. **Fork** the repository
2. **Clone** your fork locally  
3. **Create** a feature branch
4. **Make** your improvements
5. **Submit** a pull request

## 📞 **Connect With Me**

**Akash Dutta**
- 🐙 **GitHub:** [@Akash-Dutta07](https://github.com/Akash-Dutta07)
- 💼 **LinkedIn:** [Connect with me](https://linkedin.com/in/your-profile)
- 🌐 **Portfolio:** [View my other projects](https://github.com/Akash-Dutta07)

---

⭐ **Found this project helpful? Please consider starring the repository!**

*This project showcases production-ready full-stack ML development with modern Python frameworks, demonstrating both technical depth and practical deployment skills.*