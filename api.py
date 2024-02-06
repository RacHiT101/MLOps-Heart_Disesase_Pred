from flask import Flask, request, jsonify
from pipelines.deployment_pipeline import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        input_data = request.json  # Assuming input data is in JSON format
        prediction = predict(input_data)
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/hello',methods=['GET'])    

def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)
