import joblib
import streamlit as st
import pandas as pd

file_path = "pipeline.pkl"
loaded_pipeline = joblib.load(file_path)
def main():
    st.title("Heart Disease Prediction")

    # Input Data
    age = st.number_input("Age", min_value=0, step=1)
    sex = st.selectbox("Sex", [0, 1])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", min_value=0, step=1)
    chol = st.number_input("Serum Cholesterol", min_value=0, step=1)
    fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
    restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, step=1)
    exang = st.selectbox("Exercise-Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, step=0.1)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, step=1)
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })

    # Perform prediction (you can replace this with your actual model)
    prediction = loaded_pipeline.predict(input_data)  # Replace with your model prediction (1 for unhealthy, 0 for healthy)

    # Display prediction
    if prediction == 1:
        st.write("**Prediction: Unhealthy**")
    else:
        st.write("**Prediction: Healthy**")

if __name__ == "__main__":
    main()
