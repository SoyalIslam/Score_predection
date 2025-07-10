import streamlit as st
import joblib
import numpy as np
st.title("📚 Student Exam Score Predictor")

model = joblib.load("Basemodel.pkl")

attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=75)
previous_score = st.number_input("Previous Exam Score", min_value=0, max_value=100, value=70)
hours_studied = st.slider("Hours Studied", 0, 24, 4)

if st.button("Predict Exam Score"):
    input_data = np.array([[attendance, previous_score, hours_studied]])
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Exam Score: {round(float(prediction[0]), 2)}")
