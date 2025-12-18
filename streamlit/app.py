import streamlit as st
import requests
import os

st.title("Diabetes Prediction")

# API URL switches automatically
API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

pregnancies = st.number_input("Pregnancies", 0, 20, 2)
glucose = st.number_input("Glucose", 0.0, 300.0, 120.0)
blood_pressure = st.number_input("Blood Pressure", 0.0, 200.0, 70.0)
skin_thickness = st.number_input("Skin Thickness", 0.0, 100.0, 20.0)
insulin = st.number_input("Insulin", 0.0, 900.0, 80.0)
bmi = st.number_input("BMI", 0.0, 70.0, 30.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 0, 120, 33)

if st.button("Predict"):
    payload = {
        "features": [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        ]
    }

    try:
        res = requests.post(API_URL, json=payload, timeout=10)
        res.raise_for_status()
        result = res.json()

        label = "Diabetic" if result["prediction"] == 1 else "Not Diabetic"
        st.success(f"Prediction: {label}")
        st.info(f"Probability: {result['probability']:.2f}")

    except Exception as e:
        st.error(f"API Error: {e}")
