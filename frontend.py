import streamlit as st
import pandas as pd
import joblib
import os
st.set_page_config(page_title="Metro Traffic Volume Predictor", layout="wide")

# Load the model
@st.cache_resource
def load_model():
    """Load the trained model pipeline"""
    try:
        model_pipeline = joblib.load('traffic_model_pipeline.joblib')
        return model_pipeline
    except FileNotFoundError:
        st.error("Model file 'traffic_model_pipeline.joblib' not found. Please ensure the model file is in the repository.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load model
model_pipeline = load_model()

st.title("🚇 Metro Interstate Traffic Volume Predictor")

st.markdown("""
This app predicts the hourly traffic volume on a metropolitan interstate highway.
Use the sidebar to input the conditions and see the predicted traffic volume.
""")

if model_pipeline is None:
    st.stop()

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
    st.info(f"*Temperature:* {input_data['temp']} K")
    st.info(f"*Hour:* {input_data['hour']}:00")
with col2:
    st.info(f"*Weather:* {input_data['weather_main']}")
    st.info(f"*Day:* {day_options[input_data['day_of_week']]}")
with col3:
    st.info(f"*Holiday:* {input_data['holiday']}")
    st.info(f"*Rush Hour:* {'Yes' if input_data['is_rush_hour'] == 1 else 'No'}")

if st.button("Predict Traffic Volume", key="predict_button"):
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Make prediction
        prediction = model_pipeline.predict(input_df)
        predicted_volume = int(prediction[0])
        
        st.success("**Predicted Traffic Volume:**")
        st.markdown(f"<h2 style='text-align: center; color: green;'>{predicted_volume:,} vehicles/hour</h2>", unsafe_allow_html=True)
        
        # Add some additional context
        if predicted_volume > 4000:
            st.warning("⚠️ High traffic volume expected!")
        elif predicted_volume < 1500:
            st.info("ℹ️ Low traffic volume expected.")
        else:
            st.success("✅ Moderate traffic volume expected.")
            
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        st.info("Please check that all input values are valid.")
