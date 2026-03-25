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

# ──────────────────────────────────────────────────────────────
# Load JSON Data
# ──────────────────────────────────────────────────────────────
with open('symptoms.json') as f:
    all_symptoms = json.load(f)

with open('disease_classes.json') as f:
    disease_classes = json.load(f)

with open('skin_classes.json') as f:
    skin_classes = json.load(f)

skin_class_names = {v: k for k, v in skin_classes.items()}

# ──────────────────────────────────────────────────────────────
# Symptom Mapping - Converts app display names to API names
# ──────────────────────────────────────────────────────────────
SYMPTOM_MAPPING = {
    "Fever": "high_fever",
    "Headache": "headache",
    "Fatigue": "fatigue",
    "Body Ache": "body_ache",
    "Chills": "chills",
    "Sweating": "sweating",
    "Weight Loss": "weight_loss",
    "Loss of Appetite": "loss_of_appetite",
    "High Temperature": "high_fever",
    "Cough": "cough",
    "Shortness of Breath": "breathlessness",
    "Sore Throat": "throat_irritation",
    "Runny Nose": "runny_nose",
    "Loss of Smell": "loss_of_smell",
    "Loss of Taste": "loss_of_smell",
    "Chest Pain": "chest_pain",
    "Nausea": "nausea",
    "Vomiting": "vomiting",
    "Diarrhea": "diarrhoea",
    "Stomach Pain": "stomach_pain",
    "Jaundice": "yellowing_of_eyes",
    "Dark Urine": "dark_urine",
    "Palpitations": "palpitations",
    "Chest Tightness": "chest_pain",
    "Swelling": "swelling_joints",
    "Dizziness": "dizziness",
    "Skin Rash": "skin_rash",
    "Itching": "itching",
    "Eye Redness": "redness_of_eyes",
    "Confusion": "altered_sensorium",
    "Stiff Neck": "stiff_neck",
    "Sensitivity to Light": "photophobia",
    "Blurred Vision": "blurred_and_distorted_vision",
    "Muscle Weakness": "weakness_of_one_body_side",
    "Excessive Thirst": "excessive_hunger",
    "Frequent Urination": "polyuria",
    "Joint Pain": "joint_pain",
    "Back Pain": "back_pain",
    "Ear Pain": "pain_behind_the_eyes",
    "Toothache": "tooth_ache",
    "Anxiety": "anxiety",
    "Muscle Pain": "muscle_pain"
}

# ──────────────────────────────────────────────────────────────
# Load Medicine Database
# ──────────────────────────────────────────────────────────────
try:
    from medicines_data import MEDICINES, get_medicine_info, search_medicines, get_all_medicines
    MEDICINES_AVAILABLE = True
    print(f"✅ Medicine database loaded with {len(MEDICINES)} medicines")
except Exception as e:
    print(f"⚠️ Medicine database error: {e}")
    MEDICINES_AVAILABLE = False

# ──────────────────────────────────────────────────────────────
# Load ML Models at Startup
# ──────────────────────────────────────────────────────────────
print("Loading ML models...")

# Load disease model
disease_model = joblib.load('disease_model.pkl')
print("✅ Disease model loaded")

# Load severity models
severity_model = joblib.load('severity_model.pkl')
severity_disease_encoder = joblib.load('severity_disease_encoder.pkl')
severity_label_encoder = joblib.load('severity_label_encoder.pkl')
print("✅ Severity models loaded")

# Load X-Ray model
xray_model = tf.keras.models.load_model('xray_model_best.h5')
print("✅ X-Ray model loaded")

# Load Skin model
skin_model = tf.keras.models.load_model('skin_model_best.h5')
print("✅ Skin model loaded")

print("🎉 All models loaded successfully!")

# ──────────────────────────────────────────────────────────────
# Helper Functions
# ──────────────────────────────────────────────────────────────
def preprocess_image(file, size):
    """Preprocess image for model prediction"""
    img = Image.open(io.BytesIO(file.read())).resize(size).convert('RGB')
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def convert_symptoms(symptoms_list):
    """Convert display symptoms to API symptoms"""
    converted = []
    for s in symptoms_list:
        if s in SYMPTOM_MAPPING:
            converted.append(SYMPTOM_MAPPING[s])
        else:
            converted.append(s.lower().replace(" ", "_"))
    return converted

# ──────────────────────────────────────────────────────────────
# Home Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return jsonify({
        "status": "HealthMate API is running",
        "version": "2.0",
        "endpoints": {
            "predict": "/predict (POST)",
            "symptoms": "/symptoms (GET)",
            "analyze-xray": "/analyze-xray (POST)",
            "analyze-skin": "/analyze-skin (POST)",
            "doctors": "/doctors (GET)",
            "medicines": "/medicines (GET)",
            "medicine-info": "/medicine-info (GET/POST)",
            "medicines-search": "/medicines-search (GET/POST)",
            "medicines-all": "/medicines-all (GET)",
            "medicine-categories": "/medicine-categories (GET)",
            "mental-health": "/mental-health (POST)"
        }
    })

# ──────────────────────────────────────────────────────────────
# Symptoms Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({"symptoms": all_symptoms})

# ──────────────────────────────────────────────────────────────
# Disease Prediction Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        symptoms = data.get('symptoms', [])
        if not symptoms:
            return jsonify({"error": "No symptoms provided"}), 400
        
        # Convert symptoms to API format
        converted_symptoms = convert_symptoms(symptoms)
        
        # Create input vector
        input_vector = [1 if s in converted_symptoms else 0 for s in all_symptoms]
        input_array = np.array(input_vector).reshape(1, -1)
        
        # Predict disease
        prediction = disease_model.predict(input_array)[0]
        disease = disease_classes[prediction]
        
        # Get severity
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

# ──────────────────────────────────────────────────────────────
# X-Ray Analysis Endpoint
# ──────────────────────────────────────────────────────────────
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

# ──────────────────────────────────────────────────────────────
# Skin Analysis Endpoint
# ──────────────────────────────────────────────────────────────
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

# ──────────────────────────────────────────────────────────────
# Doctors Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/doctors', methods=['GET', 'POST'])
def doctors():
    specialty = request.args.get('specialty', 'all')
    doctors_list = [
        {"id": 1, "name": "Dr. Rajesh Kumar", "specialty": "General Physician", "hospital": "Apollo Hospitals", "experience": 12, "rating": 4.8, "fee": 500, "distance": 1.2, "available": True},
        {"id": 2, "name": "Dr. Priya Sharma", "specialty": "Cardiologist", "hospital": "Fortis Heart Institute", "experience": 15, "rating": 4.9, "fee": 800, "distance": 2.0, "available": True},
        {"id": 3, "name": "Dr. Amit Desai", "specialty": "Gastroenterologist", "hospital": "Manipal Hospital", "experience": 10, "rating": 4.7, "fee": 700, "distance": 3.1, "available": True},
        {"id": 4, "name": "Dr. Sneha Patel", "specialty": "Dermatologist", "hospital": "Skin Care Clinic", "experience": 8, "rating": 4.6, "fee": 600, "distance": 1.5, "available": True},
        {"id": 5, "name": "Dr. Vikram Singh", "specialty": "Neurologist", "hospital": "City Hospital", "experience": 20, "rating": 4.9, "fee": 1000, "distance": 4.0, "available": False},
        {"id": 6, "name": "Dr. Meera Joshi", "specialty": "Pediatrician", "hospital": "Kids Care Hospital", "experience": 14, "rating": 4.8, "fee": 600, "distance": 2.5, "available": True},
        {"id": 7, "name": "Dr. Rohan Mehta", "specialty": "Orthopedic", "hospital": "Bone & Joint Clinic", "experience": 11, "rating": 4.7, "fee": 750, "distance": 3.5, "available": True},
        {"id": 8, "name": "Dr. Anita Rao", "specialty": "Gynecologist", "hospital": "Women Care Hospital", "experience": 16, "rating": 4.9, "fee": 900, "distance": 2.8, "available": True}
    ]
    if specialty and specialty != 'all':
        doctors_list = [d for d in doctors_list if d['specialty'].lower() == specialty.lower()]
    return jsonify({"doctors": doctors_list})

# ──────────────────────────────────────────────────────────────
# Medicines Endpoint (Simple List)
# ──────────────────────────────────────────────────────────────
@app.route('/medicines', methods=['GET', 'POST'])
def medicines():
    query = request.args.get('q', '').lower()
    medicines_list = [
        {"name": "Paracetamol", "uses": "Fever, headache, pain relief", "dosage": "500mg every 6 hours", "warnings": "Do not exceed 4g per day"},
        {"name": "Ibuprofen", "uses": "Pain, inflammation, fever", "dosage": "400mg every 8 hours", "warnings": "Take with food"},
        {"name": "Amoxicillin", "uses": "Bacterial infections", "dosage": "500mg every 8 hours", "warnings": "Complete full course"},
        {"name": "Cetirizine", "uses": "Allergies, runny nose", "dosage": "10mg once daily", "warnings": "May cause drowsiness"},
        {"name": "Omeprazole", "uses": "Acidity, stomach ulcers", "dosage": "20mg before meals", "warnings": "Take 30 minutes before eating"},
        {"name": "Metformin", "uses": "Type 2 diabetes", "dosage": "500mg twice daily", "warnings": "Take with meals"},
        {"name": "Aspirin", "uses": "Pain, fever, blood thinning", "dosage": "75-300mg daily", "warnings": "Not for children under 16"},
        {"name": "Azithromycin", "uses": "Bacterial infections", "dosage": "500mg once daily for 3 days", "warnings": "Complete full course"},
        {"name": "Dolo 650", "uses": "Fever, body pain", "dosage": "650mg every 6 hours", "warnings": "Do not exceed 4 tablets per day"},
        {"name": "Crocin", "uses": "Fever, headache", "dosage": "500mg every 4-6 hours", "warnings": "Max 8 tablets per day"},
        {"name": "Combiflam", "uses": "Pain, fever, inflammation", "dosage": "1 tablet every 8 hours", "warnings": "Take with food"}
    ]
    if query:
        medicines_list = [m for m in medicines_list if query in m['name'].lower()]
    return jsonify({"medicines": medicines_list})

# ──────────────────────────────────────────────────────────────
# Medicine Info Endpoint (Detailed from Database)
# ──────────────────────────────────────────────────────────────
@app.route('/medicine-info', methods=['GET', 'POST'])
def medicine_info():
    """Get detailed information about a specific medicine"""
    try:
        if not MEDICINES_AVAILABLE:
            return jsonify({"error": "Medicine database temporarily unavailable"}), 503
        
        if request.method == 'GET':
            medicine_name = request.args.get('name', '')
        else:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid request body"}), 400
            medicine_name = data.get('name', '')
        
        if not medicine_name:
            return jsonify({"error": "Medicine name is required"}), 400
        
        medicine = get_medicine_info(medicine_name)
        
        if not medicine:
            return jsonify({"error": f"Medicine '{medicine_name}' not found"}), 404
        
        return jsonify(medicine)
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# ──────────────────────────────────────────────────────────────
# Medicine Search Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/medicines-search', methods=['GET', 'POST'])
def medicines_search():
    """Search for medicines by name"""
    try:
        if not MEDICINES_AVAILABLE:
            return jsonify({"error": "Medicine database temporarily unavailable"}), 503
        
        if request.method == 'GET':
            query = request.args.get('q', '')
        else:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid request body"}), 400
            query = data.get('query', '')
        
        if not query:
            return jsonify({"error": "Search query is required"}), 400
        
        results = search_medicines(query)
        
        return jsonify({
            "query": query,
            "count": len(results),
            "results": results
        })
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# ──────────────────────────────────────────────────────────────
# All Medicines Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/medicines-all', methods=['GET'])
def medicines_all():
    """Get list of all available medicines"""
    try:
        if not MEDICINES_AVAILABLE:
            return jsonify({"error": "Medicine database temporarily unavailable"}), 503
        
        all_medicines = get_all_medicines()
        
        return jsonify({
            "count": len(all_medicines),
            "medicines": all_medicines
        })
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# ──────────────────────────────────────────────────────────────
# Medicine Categories Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/medicine-categories', methods=['GET'])
def medicine_categories():
    """Get medicines grouped by category"""
    try:
        if not MEDICINES_AVAILABLE:
            return jsonify({"error": "Medicine database temporarily unavailable"}), 503
        
        categories = {
            "Pain & Fever": ["paracetamol", "ibuprofen", "aspirin", "dolo_650"],
            "Antibiotics": ["amoxicillin", "azithromycin", "ciprofloxacin"],
            "Allergy": ["cetirizine"],
            "Cold & Cough": ["cough_syrup"],
            "Stomach": ["omeprazole", "ranitidine"],
            "Diabetes": ["metformin", "insulin"],
            "Blood Pressure": ["amlodipine", "lisinopril"],
            "Vitamins": ["vitamin_c", "vitamin_d", "calcium"],
            "Heart": ["aspirin"]
        }
        
        result = {}
        for category, medicine_ids in categories.items():
            medicines_in_category = []
            for mid in medicine_ids:
                if mid in MEDICINES:
                    medicines_in_category.append({
                        "id": mid,
                        "name": MEDICINES[mid]["name"],
                        "uses": MEDICINES[mid]["uses"][:2]
                    })
            if medicines_in_category:
                result[category] = medicines_in_category
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# ──────────────────────────────────────────────────────────────
# Mental Health Assessment Endpoint
# ──────────────────────────────────────────────────────────────
@app.route('/mental-health', methods=['POST'])
def mental_health():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        answers = data.get('answers', [])
        if not answers:
            return jsonify({"error": "No answers provided"}), 400
        
        score = sum(answers)
        
        if score <= 9:
            result = "Minimal"
            advice = "You seem to be doing well mentally! Continue maintaining healthy habits like regular exercise, good sleep, and social connections."
        elif score <= 19:
            result = "Mild"
            advice = "You're experiencing mild symptoms. Consider talking to someone you trust, practicing relaxation techniques, or speaking with a counselor."
        elif score <= 29:
            result = "Moderate"
            advice = "Moderate symptoms detected. We recommend consulting a mental health professional for proper evaluation and support."
        else:
            result = "Severe"
            advice = "Severe symptoms detected. Please seek immediate professional help. Contact a mental health crisis helpline or visit your nearest hospital."
        
        return jsonify({
            "score": score,
            "result": result,
            "advice": advice
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ──────────────────────────────────────────────────────────────
# Run App
# ──────────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')