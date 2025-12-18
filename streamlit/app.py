import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Prediction", layout="centered")

st.title("Diabetes Prediction")

# LOCAL FastAPI endpoint
# API_URL = "http://localhost:8000/predict"
API_URL = "http://housing-api:8000/predict"


pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=2)
glucose = st.number_input("Glucose", min_value=0.0, max_value=300.0, value=120.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=70.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0, max_value=100.0, value=20.0)
insulin = st.number_input("Insulin", min_value=0.0, max_value=900.0, value=80.0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=30.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=33)

st.caption(
    "Input order: Pregnancies, Glucose, Blood Pressure, "
    "Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age"
)

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
        response = requests.post(API_URL, json=payload, timeout=5)
        response.raise_for_status()
        result = response.json()

        label = "Diabetic" if result["prediction"] == 1 else "Not Diabetic"
        st.success(f"Prediction: {label}")
        st.info(f"Probability: {result['probability']:.2f}")

    except requests.exceptions.RequestException as e:
        st.error("Could not connect to FastAPI server.")
        st.error(str(e))
