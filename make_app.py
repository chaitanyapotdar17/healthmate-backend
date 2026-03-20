content = """from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np

app = Flask(__name__)
CORS(app)

with open('symptoms.json') as f:
    all_symptoms = json.load(f)
with open('disease_classes.json') as f:
    disease_classes = json.load(f)

@app.route('/')
def home():
    return jsonify({"status": "HealthMate API is running"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        import joblib
        disease_model = joblib.load('disease_model.pkl')
        severity_model = joblib.load('severity_model.pkl')
        severity_disease_encoder = joblib.load('severity_disease_encoder.pkl')
        severity_label_encoder = joblib.load('severity_label_encoder.pkl')
        data = request.json
        symptoms = data.get('symptoms', [])
        input_vector = [1 if s in symptoms else 0 for s in all_symptoms]
        input_array = np.array(input_vector).reshape(1, -1)
        prediction = disease_model.predict(input_array)[0]
        disease = disease_classes[prediction]
        try:
            disease_encoded = severity_disease_encoder.transform([disease])[0]
            severity_pred = severity_model.predict([[disease_encoded]])[0]
            severity = severity_label_encoder.inverse_transform([severity_pred])[0]
        except:
            severity = "Medium"
        return jsonify({"disease": disease, "severity": severity})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({"symptoms": all_symptoms})

@app.route('/analyze-xray', methods=['POST'])
def analyze_xray():
    return jsonify({"result": "Unavailable", "confidence": 0}), 503

@app.route('/analyze-skin', methods=['POST'])
def analyze_skin():
    return jsonify({"result": "Unavailable", "confidence": 0}), 503

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""

with open('app.py', 'w') as f:
    f.write(content)
print('app.py created successfully!')