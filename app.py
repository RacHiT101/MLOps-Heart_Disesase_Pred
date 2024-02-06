import joblib
import streamlit as st
import pandas as pd
from pipelines.deployment_pipeline import predict

file_path = "pipelines/pipeline_1.pkl"
loaded_pipeline = joblib.load(file_path)

def main():
    st.title("Heart Disease Prediction")

    # Input Data
    age = st.number_input("Age", min_value=0, step=1)
    sex = st.selectbox("Sex", {"Male": 0, "Female": 1})
    cp = st.selectbox("Chest Pain Type", {"Typical angina": 0, "Atypical angina": 1 ,"Non-anginal pain" : 2,"Asymptomatic": 3})
    trestbps = st.number_input("Resting Blood Pressure", min_value=0, step=1)
    chol = st.number_input("Serum Cholesterol", min_value=0, step=1)
    fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
    restecg = st.selectbox("Resting Electrocardiographic Results", {"Normal": 0,"Having ST-T wave abnormality": 1,"Showing probable or definite left ventricular hypertrophy": 2})
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, step=1)
    exang = st.selectbox("Exercise-Induced Angina", {"No":0,"Yes":1})
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, step=0.1)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", {"Upsloping": 0,"Flat":1,"Downsloping":2 })
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, step=1)
    thal = st.selectbox("Thalassemia", {"Normal":0,"Fixed defect": 1,"Reversible defect":2,"Not described":3})

    input_data = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    # Perform prediction
    prediction = loaded_pipeline.predict(input_data)

    if prediction == 1:
        st.write("**Prediction: Presence of disease**")
    else:
        st.write("**Prediction: No disease**")

if __name__ == "__main__":
    main()
