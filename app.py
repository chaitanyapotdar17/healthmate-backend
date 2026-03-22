from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np
import os

app = Flask(__name__)
CORS(app)

with open('symptoms.json') as f:
    all_symptoms = json.load(f)
with open('disease_classes.json') as f:
    disease_classes = json.load(f)
with open('skin_classes_sklearn.json') as f:
    skin_classes = json.load(f)

@app.route('/')
def home():
    return jsonify({"status": "HealthMate API is running"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        import joblib
        if not os.path.exists('disease_model.pkl'):
            return jsonify({"error": "Model not found"}), 503
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
    try:
        import joblib
        from PIL import Image
        import io
        if not os.path.exists('xray_model_sklearn.pkl'):
            return jsonify({"error": "Model not found"}), 503
        xray_model = joblib.load('xray_model_sklearn.pkl')
        file = request.files['image']
        img = Image.open(io.BytesIO(file.read())).resize((32, 32)).convert('RGB')
        img_array = np.array(img).flatten() / 255.0
        img_array = img_array.reshape(1, -1)
        prediction = xray_model.predict(img_array)[0]
        probability = xray_model.predict_proba(img_array)[0]
        result = "Pneumonia" if prediction == 1 else "Normal"
        confidence = float(max(probability)) * 100
        return jsonify({"result": result, "confidence": round(confidence, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analyze-skin', methods=['POST'])
def analyze_skin():
    try:
        import joblib
        from PIL import Image
        import io
        if not os.path.exists('skin_model_sklearn.pkl'):
            return jsonify({"error": "Model not found"}), 503
        skin_model = joblib.load('skin_model_sklearn.pkl')
        file = request.files['image']
        img = Image.open(io.BytesIO(file.read())).resize((32, 32)).convert('RGB')
        img_array = np.array(img).flatten() / 255.0
        img_array = img_array.reshape(1, -1)
        prediction = skin_model.predict(img_array)[0]
        probability = skin_model.predict_proba(img_array)[0]
        result = skin_classes[prediction]
        confidence = float(max(probability)) * 100
        return jsonify({"result": result, "confidence": round(confidence, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
