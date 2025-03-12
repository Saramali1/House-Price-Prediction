import streamlit as st
import requests
import time

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

st.markdown("""
    <style>
        body {background-color: black; color: white;}
        h1 {margin-top: 0px !important;}
        .main {background-color: #1e1e1e; padding-top: 0px !important; border-radius: 2px !important;}
        .stButton>button {border-radius: 8px; background-color: #f2e01b; color: black; font-size: 16px; width: 100%;}
        .stButton>button:hover {background-color: #f2e01b;color: black}
        .stNumberInput>div>input {background-color: #333333; color: white;}
        .stAlert {display: flex;justify-content: center;}
    </style>
""", unsafe_allow_html=True)

st.title("🏡 House Price Prediction")
st.markdown("Enter details below to predict the house price:")

col1, col2 = st.columns(2)

with col1:
    med_inc = st.number_input("Median Income", value=0.0, format="%.2f")
    house_age = st.number_input("House Age", value=0.0, format="%.2f")
    ave_rooms = st.number_input("Average Rooms", value=0.0, format="%.2f")
    ave_bedrms = st.number_input("Average Bedrooms", value=0.0, format="%.2f")

with col2:
    population = st.number_input("Population", value=0.0, format="%.2f")
    ave_occup = st.number_input("Average Occupancy", value=0.0, format="%.2f")
    latitude = st.number_input("Latitude", value=0.0, format="%.2f")
    longitude = st.number_input("Longitude", value=0.0, format="%.2f")

st.markdown("<br>", unsafe_allow_html=True)
col_center = st.columns([1, 2, 1])
with col_center[1]:
    if st.button("Predict Price"):
        progress_bar = st.progress(0)
        
        for percent_complete in range(0, 101, 10):
            time.sleep(0.1)
            progress_bar.progress(percent_complete)

        input_data = {
            "MedInc": med_inc,
            "HouseAge": house_age,
            "AveRooms": ave_rooms,
            "AveBedrms": ave_bedrms,
            "Population": population,
            "AveOccup": ave_occup,
            "Latitude": latitude,
            "Longitude": longitude
        }
        response = requests.post("http://3.110.108.39:8000/predict", json=input_data)

        progress_bar.empty()
        
        if response.status_code == 200:
            price = response.json()['predicted_price']
            st.success(f"✅ Predicted House Price: **{price}**")

        else:
            st.error("❌ Error making prediction")

st.markdown("""
    <div style="text-align: center; font-size: 16px; font-weight: bold; color: white; margin-top: 10px;">
        Developed by <span style="color: #f2e01b;">Sara Mali</span>
    </div>
""", unsafe_allow_html=True)

