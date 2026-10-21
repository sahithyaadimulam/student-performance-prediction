
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("student_performance_model.pkl")

st.title("Student Performance Prediction")
st.write("Predict a student's performance using study habits and previous scores.")

hours = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
previous = st.number_input("Previous Scores", min_value=0, max_value=100, value=70)
activity = st.selectbox("Extracurricular Activities", ["Yes", "No"])
sleep = st.number_input("Sleep Hours", min_value=0, max_value=24, value=7)
papers = st.number_input(
    "Sample Question Papers Practiced",
    min_value=0,
    max_value=100,
    value=3
)

if st.button("Predict Performance"):
    input_data = pd.DataFrame([{
        "Hours Studied": hours,
        "Previous Scores": previous,
        "Extracurricular Activities": 1 if activity == "Yes" else 0,
        "Sleep Hours": sleep,
        "Sample Question Papers Practiced": papers
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Performance Index: {prediction:.2f}")
