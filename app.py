from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np
import os
import joblib
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load JSON files
with open('symptoms.json') as f:
    all_symptoms = json.load(f)
with open('disease_classes.json') as f:
    disease_classes = json.load(f)
with open('skin_classes.json') as f:
    skin_classes = json.load(f)

skin_class_names = {v: k for k, v in skin_classes.items()}

# Load all models at startup
print("Loading disease model...")
disease_model = joblib.load('disease_model.pkl')
print("Loading severity model...")
severity_model = joblib.load('severity_model.pkl')
severity_disease_encoder = joblib.load('severity_disease_encoder.pkl')
severity_label_encoder = joblib.load('severity_label_encoder.pkl')
print("Loading X-Ray model...")
xray_model = tf.keras.models.load_model('xray_model_best.keras')
print("Loading Skin model...")
skin_model = tf.keras.models.load_model('skin_model_best.keras')
print("All models loaded!")

# Helper function
def preprocess_image(file, size):
    img = Image.open(io.BytesIO(file.read())).resize(size).convert('RGB')
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

# Home endpoint
@app.route('/')
def home():
    return jsonify({"status": "HealthMate API is running"})

# Symptoms endpoint
@app.route('/symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({"symptoms": all_symptoms})

# Disease prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        symptoms = data.get('symptoms', [])
        if not symptoms:
            return jsonify({"error": "No symptoms provided"}), 400
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
        return jsonify({
            "disease": disease,
            "severity": severity
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# X-Ray analysis endpoint
@app.route('/analyze-xray', methods=['POST'])
def analyze_xray():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400
        img_array = preprocess_image(file, (224, 224))
        prediction = xray_model.predict(img_array)[0][0]
        result = "Pneumonia" if prediction > 0.5 else "Normal"
        confidence = float(prediction) if prediction > 0.5 else float(1 - prediction)
        return jsonify({
            "result": result,
            "confidence": round(confidence * 100, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Skin analysis endpoint
@app.route('/analyze-skin', methods=['POST'])
def analyze_skin():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400
        img_array = preprocess_image(file, (224, 224))
        predictions = skin_model.predict(img_array)[0]
        class_idx = int(np.argmax(predictions))
        result = skin_class_names[class_idx]
        confidence = float(predictions[class_idx])
        return jsonify({
            "result": result,
            "confidence": round(confidence * 100, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Doctors endpoint
@app.route('/doctors', methods=['GET', 'POST'])
def doctors():
    specialty = request.args.get('specialty', 'all')
    doctors_list = [
        {"id": 1, "name": "Dr. Rajesh Kumar", "specialty": "General Physician",
         "hospital": "Apollo Hospitals", "experience": 12, "rating": 4.8,
         "fee": 500, "distance": 1.2, "available": True},
        {"id": 2, "name": "Dr. Priya Sharma", "specialty": "Cardiologist",
         "hospital": "Fortis Heart Institute", "experience": 15, "rating": 4.9,
         "fee": 800, "distance": 2.0, "available": True},
        {"id": 3, "name": "Dr. Amit Desai", "specialty": "Gastroenterologist",
         "hospital": "Manipal Hospital", "experience": 10, "rating": 4.7,
         "fee": 700, "distance": 3.1, "available": True},
        {"id": 4, "name": "Dr. Sneha Patel", "specialty": "Dermatologist",
         "hospital": "Skin Care Clinic", "experience": 8, "rating": 4.6,
         "fee": 600, "distance": 1.5, "available": True},
        {"id": 5, "name": "Dr. Vikram Singh", "specialty": "Neurologist",
         "hospital": "City Hospital", "experience": 20, "rating": 4.9,
         "fee": 1000, "distance": 4.0, "available": False},
        {"id": 6, "name": "Dr. Meera Joshi", "specialty": "Pediatrician",
         "hospital": "Kids Care Hospital", "experience": 14, "rating": 4.8,
         "fee": 600, "distance": 2.5, "available": True},
        {"id": 7, "name": "Dr. Rohan Mehta", "specialty": "Orthopedic",
         "hospital": "Bone & Joint Clinic", "experience": 11, "rating": 4.7,
         "fee": 750, "distance": 3.5, "available": True},
        {"id": 8, "name": "Dr. Anita Rao", "specialty": "Gynecologist",
         "hospital": "Women Care Hospital", "experience": 16, "rating": 4.9,
         "fee": 900, "distance": 2.8, "available": True}
    ]
    if specialty and specialty != 'all':
        doctors_list = [d for d in doctors_list
                       if d['specialty'].lower() == specialty.lower()]
    return jsonify({"doctors": doctors_list})

# Medicines endpoint
@app.route('/medicines', methods=['GET', 'POST'])
def medicines():
    query = request.args.get('q', '').lower()
    medicines_list = [
        {"name": "Paracetamol", "uses": "Fever, headache, pain relief",
         "dosage": "500mg every 6 hours", "warnings": "Do not exceed 4g per day"},
        {"name": "Ibuprofen", "uses": "Pain, inflammation, fever",
         "dosage": "400mg every 8 hours", "warnings": "Take with food"},
        {"name": "Amoxicillin", "uses": "Bacterial infections",
         "dosage": "500mg every 8 hours", "warnings": "Complete full course"},
        {"name": "Cetirizine", "uses": "Allergies, runny nose",
         "dosage": "10mg once daily", "warnings": "May cause drowsiness"},
        {"name": "Omeprazole", "uses": "Acidity, stomach ulcers",
         "dosage": "20mg before meals", "warnings": "Take 30 minutes before eating"},
        {"name": "Metformin", "uses": "Type 2 diabetes",
         "dosage": "500mg twice daily", "warnings": "Take with meals"},
        {"name": "Aspirin", "uses": "Pain, fever, blood thinning",
         "dosage": "75-300mg daily", "warnings": "Not for children under 16"},
        {"name": "Azithromycin", "uses": "Bacterial infections",
         "dosage": "500mg once daily for 3 days", "warnings": "Complete full course"},
        {"name": "Pantoprazole", "uses": "Acid reflux, ulcers",
         "dosage": "40mg once daily", "warnings": "Take before breakfast"},
        {"name": "Dolo 650", "uses": "Fever, body pain",
         "dosage": "650mg every 6 hours", "warnings": "Do not exceed 4 tablets per day"},
        {"name": "Crocin", "uses": "Fever, headache",
         "dosage": "500mg every 4-6 hours", "warnings": "Max 8 tablets per day"},
        {"name": "Combiflam", "uses": "Pain, fever, inflammation",
         "dosage": "1 tablet every 8 hours", "warnings": "Take with food"}
    ]
    if query:
        medicines_list = [m for m in medicines_list
                         if query in m['name'].lower()]
    return jsonify({"medicines": medicines_list})

# Mental health endpoint
@app.route('/mental-health', methods=['POST'])
def mental_health():
    try:
        data = request.json
        answers = data.get('answers', [])
        score = sum(answers)
        if score <= 9:
            result = "Minimal"
            advice = "You seem to be doing well mentally!"
        elif score <= 19:
            result = "Mild"
            advice = "Consider talking to someone you trust."
        elif score <= 29:
            result = "Moderate"
            advice = "We recommend consulting a mental health professional."
        else:
            result = "Severe"
            advice = "Please seek immediate professional help."
        return jsonify({
            "score": score,
            "result": result,
            "advice": advice
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
