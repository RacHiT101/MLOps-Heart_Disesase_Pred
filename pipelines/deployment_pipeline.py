import joblib
import pandas as pd

# Load your trained pipeline
with open('pipelines/pipeline_1.pkl', 'rb') as f:
    pipeline = joblib.load(f)

def predict(input_data):
    try:
        # Preprocess input data
        input_df = pd.DataFrame(input_data, index=[0])  # Convert input data to DataFrame
        preprocessed_data = pipeline.transform(input_df)

        # Make predictions
        predictions = pipeline.predict(preprocessed_data)
        return predictions.tolist()
    except Exception as e:
        return {'error': str(e)}
