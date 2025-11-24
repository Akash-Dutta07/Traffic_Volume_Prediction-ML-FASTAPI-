import streamlit as st
import requests
import json

st.set_page_config(page_title="Metro Traffic Volume Predictor (API Version)", layout="wide")
st.title("🚇 Metro Interstate Traffic Volume Predictor")
st.caption("🔗 **FastAPI Integration Version** - This version demonstrates API consumption")

st.markdown("""
This app predicts the hourly traffic volume on a metropolitan interstate highway.
**This version uses FastAPI backend** - make sure to run `uvicorn api:app --reload` first.
""")

# API Status Check
@st.cache_data(ttl=30)  # Cache for 30 seconds
def check_api_status():
    """Check if FastAPI server is running"""
    try:
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        return response.status_code == 200
    except:
        return False

api_online = check_api_status()

if api_online:
    st.success("✅ FastAPI server is running at http://127.0.0.1:8000")
    st.markdown("📚 **API Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)")
else:
    st.error("❌ FastAPI server is not running. Please start it with: `uvicorn api:app --reload`")
    st.info("💡 For cloud deployment, use `streamlit run frontend.py` instead.")

st.sidebar.header("Input Features")

holiday_options = ['None', 'Martin Luther King Jr Day', 'Columbus Day',
                   'State Fair', 'Veterans Day', 'Thanksgiving Day',
                   'Christmas Day', 'New Years Day', 'Washingtons Birthday',
                   'Memorial Day', 'Independence Day', 'Labor Day']

weather_options = ['Clouds', 'Clear', 'Rain', 'Drizzle', 'Mist', 'Haze',
                   'Fog', 'Thunderstorm', 'Snow', 'Squall', 'Smoke']

day_options = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
               4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

def user_input_features():
    """
    Creates sidebar widgets and returns a dictionary of inputs.
    """
    holiday = st.sidebar.selectbox("Holiday", holiday_options)
    temp_f = st.sidebar.slider("Temperature (°F)", min_value=-20, max_value=120, value=75)

    temp_k = round((temp_f - 32) * 5/9 + 273.15, 2)

    weather_main = st.sidebar.selectbox("Main Weather Condition", weather_options)
    clouds_all = st.sidebar.slider("Cloud Cover (%)", min_value=0, max_value=100, value=40)
    hour = st.sidebar.slider("Hour of the Day (0-23)", min_value=0, max_value=23, value=9)
    day_of_week = st.sidebar.selectbox("Day of the Week", options=list(day_options.keys()), format_func=lambda x: day_options[x])
    month = st.sidebar.slider("Month of the Year", min_value=1, max_value=12, value=10)

    is_rush_hour = 1 if (7 <= hour <= 9) or (16 <= hour <= 18) else 0

    data = {
        'holiday': holiday,
        'temp': temp_k,
        'rain_1h': 0.0,
        'snow_1h': 0.0,
        'clouds_all': clouds_all,
        'weather_main': weather_main,
        'hour': hour,
        'day_of_week': day_of_week,
        'month': month,
        'is_rush_hour': is_rush_hour
    }
    return data

input_data = user_input_features()

st.subheader("Current Input Parameters")

col1, col2, col3 = st.columns(3)
with col1:
    st.info(f"**Temperature:** {input_data['temp']} K")
    st.info(f"**Hour:** {input_data['hour']}:00")
with col2:
    st.info(f"**Weather:** {input_data['weather_main']}")
    st.info(f"**Day:** {day_options[input_data['day_of_week']]}")
with col3:
    st.info(f"**Holiday:** {input_data['holiday']}")
    st.info(f"**Rush Hour:** {'Yes' if input_data['is_rush_hour'] == 1 else 'No'}")

# API Request Section
st.subheader("🔌 FastAPI Integration")

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🚀 Predict via FastAPI", disabled=not api_online, key="predict_button"):
        api_url = "http://127.0.0.1:8000/predict"
        
        with st.spinner("Making API request..."):
            try:
                headers = {"Content-Type": "application/json"}
                response = requests.post(
                    api_url, 
                    data=json.dumps(input_data), 
                    headers=headers,
                    timeout=10
                )
                response.raise_for_status()

                prediction = response.json()
                
                if 'predicted_traffic_volume' in prediction:
                    volume = prediction['predicted_traffic_volume']
                    st.success("**Predicted Traffic Volume:**")
                    st.markdown(f"<h2 style='text-align: center; color: green;'>{volume:,} vehicles/hour</h2>", unsafe_allow_html=True)
                    
                    # Add context
                    if volume > 4000:
                        st.warning("⚠️ High traffic volume expected!")
                    elif volume < 1500:
                        st.info("ℹ️ Low traffic volume expected.")
                    else:
                        st.success("✅ Moderate traffic volume expected.")
                        
                    # Show API response details
                    with st.expander("📋 API Response Details"):
                        st.json(prediction)
                        st.code(f"POST {api_url}", language="http")
                        st.code(f"Status Code: {response.status_code}")
                        
                else:
                    st.error(f"Unexpected API response: {prediction}")

            except requests.exceptions.RequestException as e:
                st.error(f"❌ **API Connection Error**")
                st.error(f"Could not connect to FastAPI server: {str(e)}")
                st.info("💡 Make sure the FastAPI server is running with: `uvicorn api:app --reload`")
            except Exception as e:
                st.error(f"❌ **Error**: {str(e)}")

with col2:
    st.info("**🛠️ API Development Features:**")
    st.markdown("""
    - ✅ **RESTful API** design
    - ✅ **Pydantic validation**
    - ✅ **Error handling**
    - ✅ **Auto documentation**
    - ✅ **JSON responses**
    - ✅ **CORS support**
    """)

# Development Information
st.divider()
st.subheader("👨‍💻 Development Information")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**🔧 Local Development:**")
    st.code("""
    # Start FastAPI server
    uvicorn api:app --reload
    
    # Start this Streamlit app
    streamlit run frontend_api.py
    """, language="bash")

with col2:
    st.markdown("**📡 API Endpoints:**")
    st.code("""
    GET  /           - Health check
    POST /predict    - Make prediction
    GET  /docs       - API documentation
    GET  /redoc      - Alternative docs
    """, language="http")

if api_online:
    st.success("🎯 **This demonstrates full-stack API development with FastAPI + Streamlit integration!**")
else:
    st.warning("⚡ Start the FastAPI server to see the full integration in action!")