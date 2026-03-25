# Complete Medicine Database - Error Free
MEDICINES = {
    # Pain & Fever
    "paracetamol": {
        "name": "Paracetamol (Acetaminophen)",
        "uses": ["Fever", "Headache", "Mild to moderate pain", "Body aches", "Toothache", "Muscle pain", "Menstrual cramps"],
        "how_to_use": "Take 500mg every 4-6 hours as needed. Do not exceed 3000mg in 24 hours. Can be taken with or without food. Swallow whole with water.",
        "dosage": "Adults: 500-1000mg every 4-6 hours. Maximum 3000mg/day. Children: 10-15mg/kg every 4-6 hours. Not for infants under 3 months without doctor advice.",
        "warnings": "Do not take with alcohol. Overdose can cause severe liver damage. Do not take with other paracetamol-containing products. Seek immediate medical help if overdose suspected.",
        "side_effects": ["Nausea (mild)", "Skin rash (rare)", "Liver damage (overdose)", "Allergic reactions (rare)"],
        "when_to_take": "At the first sign of fever or pain. For fever, take as soon as temperature rises above 100.4°F (38°C). For pain, take when pain is felt.",
        "storage": "Store at room temperature (20-25°C), away from moisture and heat. Keep out of reach of children."
    },
    
    "ibuprofen": {
        "name": "Ibuprofen (Advil, Motrin)",
        "uses": ["Fever", "Inflammation", "Muscle pain", "Joint pain", "Menstrual cramps", "Arthritis", "Headache", "Back pain", "Dental pain"],
        "how_to_use": "Take 200-400mg every 6-8 hours with food or milk to prevent stomach upset. Swallow whole, do not crush or chew. Drink a full glass of water.",
        "dosage": "Adults: 200-400mg every 6-8 hours. Maximum 1200mg/day for OTC use. Maximum 2400mg/day with prescription. Children: 5-10mg/kg every 6-8 hours.",
        "warnings": "Do not take if you have stomach ulcers, kidney problems, or are allergic to aspirin. Avoid during pregnancy (3rd trimester). May increase bleeding risk.",
        "side_effects": ["Stomach upset", "Heartburn", "Nausea", "Dizziness", "Headache", "Stomach bleeding (long term)", "Kidney problems (long term)"],
        "when_to_take": "Take with meals or milk to reduce stomach irritation. For inflammation, take regularly as prescribed at the same times each day.",
        "storage": "Store at room temperature, keep away from moisture. Do not freeze. Keep bottle tightly closed."
    },
    
    # Antibiotics
    "amoxicillin": {
        "name": "Amoxicillin",
        "uses": ["Bacterial infections", "Respiratory infections", "Ear infections", "Throat infections (strep throat)", "Urinary tract infections", "Dental infections", "Skin infections", "Pneumonia"],
        "how_to_use": "Take exactly as prescribed. Complete the full course even if you feel better. Can be taken with or without food. If stomach upset occurs, take with food.",
        "dosage": "Adults: 250-500mg every 8 hours or 500-875mg every 12 hours for 7-14 days as prescribed. Children: 20-40mg/kg/day divided every 8-12 hours.",
        "warnings": "Complete full course to prevent antibiotic resistance. Avoid if allergic to penicillin. Tell doctor if you have kidney disease, asthma, or mononucleosis.",
        "side_effects": ["Diarrhea", "Nausea", "Vomiting", "Skin rash", "Yeast infection", "Dizziness", "Headache"],
        "when_to_take": "Take at evenly spaced intervals. For 3 times daily, take every 8 hours. For twice daily, take every 12 hours. Set reminders to not miss doses.",
        "storage": "Store in a cool, dry place. Liquid form should be refrigerated and used within 14 days. Do not freeze."
    },
    
    "azithromycin": {
        "name": "Azithromycin (Zithromax, Z-Pak)",
        "uses": ["Respiratory infections", "Throat infections", "Skin infections", "Ear infections", "Pneumonia", "STDs", "Sinus infections", "Bronchitis"],
        "how_to_use": "Take on an empty stomach (1 hour before or 2 hours after meals) unless stomach upset occurs. Complete full course even if feeling better.",
        "dosage": "Usually 500mg on day 1, then 250mg days 2-5. Or 500mg daily for 3 days. Follow prescription exactly. Shake liquid well before use.",
        "warnings": "Do not take with antacids containing aluminum or magnesium (wait at least 2 hours). Avoid if allergic to macrolide antibiotics. May cause heart rhythm changes.",
        "side_effects": ["Diarrhea", "Nausea", "Abdominal pain", "Vomiting", "Headache", "Dizziness", "Taste changes"],
        "when_to_take": "Take at the same time each day. For 5-day course, follow the schedule exactly. Use a pill organizer to avoid missing doses.",
        "storage": "Store at room temperature. Liquid form can be stored at room temperature for up to 10 days. Do not freeze."
    },
    
    "ciprofloxacin": {
        "name": "Ciprofloxacin (Cipro)",
        "uses": ["Urinary tract infections", "Respiratory infections", "Skin infections", "Gastrointestinal infections", "Prostatitis", "Sinus infections", "Bone infections", "Anthrax"],
        "how_to_use": "Take 250-750mg every 12 hours. Drink plenty of water (8-10 glasses daily). Complete full course. Swallow whole, do not crush or chew.",
        "dosage": "Adults: 250-750mg twice daily for 7-14 days as prescribed. For UTIs: 250-500mg twice daily for 3-7 days.",
        "warnings": "Avoid antacids, dairy products, calcium-fortified juices within 2 hours. May increase tendon rupture risk. Avoid sun exposure. Not for children under 18.",
        "side_effects": ["Nausea", "Diarrhea", "Dizziness", "Headache", "Tendon pain", "Sun sensitivity", "Insomnia"],
        "when_to_take": "Take at evenly spaced intervals every 12 hours. Drink full glass of water. Avoid taking within 2 hours of dairy or antacids.",
        "storage": "Store at room temperature, protect from light. Do not freeze. Keep container tightly closed."
    },
    
    # Allergy
    "cetirizine": {
        "name": "Cetirizine (Zyrtec)",
        "uses": ["Seasonal allergies", "Hay fever", "Runny nose", "Sneezing", "Itchy eyes", "Hives", "Skin allergies", "Allergic rhinitis"],
        "how_to_use": "Take 10mg once daily. May cause drowsiness - avoid driving if affected. Can be taken with or without food. Swallow whole with water.",
        "dosage": "Adults and children 12+: 10mg once daily. Children 6-12 years: 5-10mg once daily. Children 2-6 years: 2.5-5mg once daily.",
        "warnings": "Avoid alcohol. May cause drowsiness - use caution when driving or operating machinery. Consult doctor if pregnant or nursing.",
        "side_effects": ["Drowsiness", "Dry mouth", "Fatigue", "Headache", "Dizziness", "Sore throat", "Stomach pain"],
        "when_to_take": "Take at the same time each day. For seasonal allergies, start taking 1 week before allergy season begins. Take at night if drowsiness occurs.",
        "storage": "Store at room temperature, protect from moisture. Keep out of reach of children."
    },
    
    # Cold & Cough
    "dolo_650": {
        "name": "Dolo 650 (Paracetamol)",
        "uses": ["Fever", "Body pain", "Headache", "Cold symptoms", "Muscle pain", "Arthritis pain", "Back pain", "Dental pain"],
        "how_to_use": "Take 650mg every 6 hours as needed for fever or pain. Do not exceed 4 tablets in 24 hours. Swallow with water. Can be taken with or without food.",
        "dosage": "1 tablet (650mg) every 6 hours when needed. Maximum 4 tablets/day. For severe pain, consult doctor for higher dose.",
        "warnings": "Do not exceed recommended dose. Avoid alcohol. Not for long-term use without doctor advice. Seek help if overdose suspected.",
        "side_effects": ["Usually well tolerated", "Nausea (rare)", "Skin rash (rare)", "Liver damage (overdose)"],
        "when_to_take": "Take when fever or pain occurs. For fever, take as soon as temperature rises. For pain, take at first sign of pain.",
        "storage": "Store in a cool, dry place away from sunlight. Keep blister pack intact until use."
    },
    
    "cough_syrup": {
        "name": "Cough Syrup (Dextromethorphan/Guaifenesin)",
        "uses": ["Dry cough", "Wet cough", "Chest congestion", "Cold symptoms", "Throat irritation", "Mucus relief", "Bronchitis symptoms"],
        "how_to_use": "Take 10-20ml every 4-6 hours as needed. Shake well before use. Drink plenty of water (8-10 glasses daily). Do not exceed 4 doses in 24 hours.",
        "dosage": "Adults: 10-20ml every 4-6 hours. Maximum 4 doses/day. Children 6-12: 5-10ml every 4-6 hours. Children under 6: As prescribed by doctor.",
        "warnings": "Do not drive after taking. Avoid alcohol. Not for children under 6 without doctor advice. If cough persists more than 7 days, see doctor.",
        "side_effects": ["Drowsiness", "Nausea", "Dizziness", "Stomach upset", "Headache", "Nervousness"],
        "when_to_take": "Take when cough is persistent. For dry cough, take as needed. For wet cough, take to loosen mucus. Take before bed if cough disrupts sleep.",
        "storage": "Store at room temperature, protect from light, keep bottle tightly closed. Do not freeze."
    },
    
    # Stomach
    "omeprazole": {
        "name": "Omeprazole (Prilosec)",
        "uses": ["Acid reflux", "Heartburn", "GERD", "Stomach ulcers", "Indigestion", "Acidity", "Zollinger-Ellison syndrome"],
        "how_to_use": "Take 20-40mg once daily before breakfast. Swallow capsule whole, do not crush, chew, or open. For delayed-release capsules, swallow whole.",
        "dosage": "Adults: 20mg once daily for 14 days. For long-term use, follow doctor's prescription. Maximum 40mg/day. Do not use for more than 14 days without doctor advice.",
        "warnings": "Do not use for more than 14 days without doctor advice. Long-term use may increase risk of bone fractures, vitamin B12 deficiency. Consult doctor if pregnant.",
        "side_effects": ["Headache", "Nausea", "Diarrhea", "Stomach pain", "Gas", "Constipation", "Dizziness", "Dry mouth"],
        "when_to_take": "Take 30-60 minutes before breakfast for best results. Take at the same time each day. If taking twice daily, take before breakfast and dinner.",
        "storage": "Store at room temperature, protect from moisture. Keep bottle tightly closed. Do not store in bathroom."
    },
    
    "ranitidine": {
        "name": "Ranitidine (Zantac)",
        "uses": ["Acid reflux", "Heartburn", "Stomach ulcers", "GERD", "Indigestion", "Acidity", "Zollinger-Ellison syndrome"],
        "how_to_use": "Take 150mg twice daily or 300mg once daily at bedtime. Can be taken with or without food. Swallow whole with water.",
        "dosage": "Adults: 150mg twice daily or 300mg at bedtime. For prevention: 150mg at bedtime. Children: As prescribed by doctor.",
        "warnings": "Do not exceed recommended dose. Avoid alcohol. Tell doctor if you have kidney disease, liver disease, or porphyria. Some formulations may contain ranitidine alternatives.",
        "side_effects": ["Headache", "Constipation", "Diarrhea", "Nausea", "Stomach pain", "Dizziness", "Insomnia"],
        "when_to_take": "Take at the same times each day. For once daily, take at bedtime. For twice daily, take with breakfast and dinner.",
        "storage": "Store at room temperature, protect from light and moisture. Keep out of reach of children."
    },
    
    # Diabetes
    "metformin": {
        "name": "Metformin (Glucophage)",
        "uses": ["Type 2 diabetes", "High blood sugar", "PCOS", "Insulin resistance", "Prediabetes", "Weight management"],
        "how_to_use": "Take with meals to reduce stomach upset. Start with 500mg once or twice daily. Swallow whole, do not crush or chew. Extended-release tablets: swallow whole.",
        "dosage": "Start 500mg once or twice daily. Increase slowly. Maximum 2000-2500mg/day as prescribed. Extended-release: Maximum 2000mg/day.",
        "warnings": "Monitor blood sugar regularly. Risk of lactic acidosis if kidneys not functioning. Stop before surgery or contrast dye procedures. Avoid alcohol.",
        "side_effects": ["Nausea", "Diarrhea", "Stomach upset", "Loss of appetite", "Metallic taste", "Gas", "Vitamin B12 deficiency (long term)"],
        "when_to_take": "Take with breakfast and dinner to reduce stomach upset and control blood sugar throughout the day. Take at same times daily.",
        "storage": "Store at room temperature, protect from moisture. Keep bottle tightly closed. Do not store in bathroom."
    },
    
    "insulin": {
        "name": "Insulin (Various Types)",
        "uses": ["Type 1 diabetes", "Type 2 diabetes", "Gestational diabetes", "High blood sugar"],
        "how_to_use": "Inject as prescribed by doctor. Rotate injection sites. Check blood sugar before each injection. Do not shake vigorously - roll between palms.",
        "dosage": "Follow doctor's prescription exactly. Dosage varies by type: Rapid-acting, Short-acting, Intermediate-acting, Long-acting. Never change dose without doctor advice.",
        "warnings": "Monitor blood sugar closely. Risk of hypoglycemia (low blood sugar). Carry sugar source always. Do not share pens or needles. Check expiration date.",
        "side_effects": ["Hypoglycemia (low blood sugar)", "Injection site reactions", "Weight gain", "Lipodystrophy (fat changes at injection site)", "Allergic reactions"],
        "when_to_take": "Follow prescribed timing. Rapid-acting: before meals. Long-acting: once or twice daily at same time. Never skip doses without doctor advice.",
        "storage": "Store unopened vials/pens in refrigerator (36-46°F). Do not freeze. Opened vials can be stored at room temperature for up to 28 days."
    },
    
    # Blood Pressure
    "amlodipine": {
        "name": "Amlodipine (Norvasc)",
        "uses": ["High blood pressure", "Chest pain", "Angina", "Heart disease", "Coronary artery disease"],
        "how_to_use": "Take 5-10mg once daily. Can be taken with or without food at the same time each day. Swallow whole, do not crush or chew.",
        "dosage": "Start 5mg once daily. Maximum 10mg/day as prescribed. Elderly: Start 2.5mg once daily. May take 2 weeks for full effect.",
        "warnings": "Do not stop suddenly without doctor advice. Monitor blood pressure regularly. Avoid grapefruit and grapefruit juice. May cause dizziness - avoid driving if affected.",
        "side_effects": ["Swelling in ankles/feet", "Dizziness", "Headache", "Flushing", "Fatigue", "Palpitations", "Nausea"],
        "when_to_take": "Take at the same time each day, preferably in the morning. Take with food if stomach upset occurs. Use pill organizer to avoid missing doses.",
        "storage": "Store at room temperature, away from light and moisture. Keep out of reach of children."
    },
    
    "lisinopril": {
        "name": "Lisinopril (Prinivil, Zestril)",
        "uses": ["High blood pressure", "Heart failure", "Heart attack recovery", "Diabetic kidney disease"],
        "how_to_use": "Take 10-40mg once daily at the same time each day. Can be taken with or without food. Swallow whole with water.",
        "dosage": "Start 10mg once daily. Maintenance 20-40mg once daily. Heart failure: Start 5mg once daily. Maximum 40mg/day.",
        "warnings": "Do not take if pregnant. May cause dry cough. Monitor kidney function. Avoid potassium supplements. May cause dizziness - rise slowly from sitting.",
        "side_effects": ["Dry cough", "Dizziness", "Headache", "Fatigue", "Nausea", "Rash", "High potassium", "Low blood pressure"],
        "when_to_take": "Take at the same time each day, preferably in the morning. If taking twice daily, take morning and evening. Use consistently.",
        "storage": "Store at room temperature, protect from moisture. Keep bottle tightly closed."
    },
    
    # Heart
    "aspirin": {
        "name": "Aspirin (Acetylsalicylic Acid)",
        "uses": ["Pain", "Fever", "Inflammation", "Heart attack prevention", "Stroke prevention", "Headache", "Menstrual cramps", "Arthritis"],
        "how_to_use": "Take 325-650mg every 4-6 hours with food. For heart protection, take 81mg daily as prescribed. Swallow whole, do not crush.",
        "dosage": "Pain: 325-650mg every 4-6 hours. Maximum 4000mg/day. Heart protection: 81mg daily (low dose). Stroke prevention: 81-325mg daily as prescribed.",
        "warnings": "Not for children under 16 due to Reye's syndrome risk. Avoid if stomach ulcers, bleeding disorders. Stop 1 week before surgery. Avoid alcohol.",
        "side_effects": ["Stomach irritation", "Heartburn", "Nausea", "Bleeding risk", "Bruising", "Ringing in ears (high doses)"],
        "when_to_take": "Take with food to reduce stomach upset. For heart protection, take at same time daily (usually morning). For pain, take when pain occurs.",
        "storage": "Store at room temperature, protect from moisture. Keep bottle tightly closed. Do not store in bathroom."
    },
    
    # Vitamins & Supplements
    "vitamin_c": {
        "name": "Vitamin C (Ascorbic Acid)",
        "uses": ["Immune support", "Cold prevention", "Antioxidant", "Wound healing", "Skin health", "Iron absorption", "Collagen production", "Scurvy prevention"],
        "how_to_use": "Take 500-1000mg daily with food. Can be taken any time of day. Swallow whole or chew as directed. Drink plenty of water.",
        "dosage": "Adults: 500-1000mg daily. Maximum 2000mg/day. Children: 40-1000mg/day based on age. Higher doses may be used for short periods during illness.",
        "warnings": "High doses may cause diarrhea. Consult doctor if pregnant, nursing, or have kidney stones. May interact with certain medications.",
        "side_effects": ["Stomach upset", "Diarrhea (high doses)", "Nausea (high doses)", "Heartburn", "Headache (high doses)"],
        "when_to_take": "Take with meals for better absorption. Can be taken any time, consistent timing helps. Divide into 2 doses for better absorption.",
        "storage": "Store in a cool, dry place away from light. Keep bottle tightly closed. Do not store in bathroom."
    },
    
    "vitamin_d": {
        "name": "Vitamin D3 (Cholecalciferol)",
        "uses": ["Bone health", "Calcium absorption", "Immune function", "Mood support", "Muscle function", "Vitamin D deficiency", "Osteoporosis prevention"],
        "how_to_use": "Take 600-2000 IU daily with food. Best taken with the largest meal of the day. Swallow whole, do not chew.",
        "dosage": "Adults: 600-2000 IU daily. For deficiency: 50,000 IU weekly for 8 weeks. Children: 400-600 IU daily. Follow doctor's prescription for high doses.",
        "warnings": "Do not exceed recommended dose without doctor advice. May interact with certain medications. Monitor calcium levels with high doses.",
        "side_effects": ["Usually well tolerated", "Nausea (high doses)", "Constipation (high doses)", "Loss of appetite (high doses)", "Confusion (very high doses)"],
        "when_to_take": "Take with the largest meal containing fat for best absorption. Take at the same time daily. Best taken in the morning.",
        "storage": "Store at room temperature, protect from light and moisture. Keep out of reach of children."
    },
    
    "calcium": {
        "name": "Calcium Carbonate",
        "uses": ["Bone health", "Osteoporosis prevention", "Calcium deficiency", "Dental health", "Muscle function", "Heart health", "Nerve function"],
        "how_to_use": "Take 500-600mg with food. For total daily dose, divide into 2-3 doses. Swallow whole with water. Do not take more than 500-600mg at once.",
        "dosage": "Adults: 1000-1200mg daily. Take in divided doses of 500-600mg each. Maximum 2000mg/day. Children: 800-1300mg/day based on age.",
        "warnings": "Do not exceed recommended dose. May interact with certain medications (wait 2-4 hours apart). Consult doctor if kidney stones history.",
        "side_effects": ["Constipation", "Gas", "Bloating", "Stomach upset", "Nausea (high doses)", "Kidney stones (very high doses)"],
        "when_to_take": "Take with meals for best absorption. Take at different times than iron supplements. Divide doses throughout the day.",
        "storage": "Store at room temperature, protect from moisture. Keep bottle tightly closed."
    }
}

# Helper Functions
def get_medicine_info(medicine_name):
    """Get detailed information about a medicine"""
    if not medicine_name:
        return None
    
    medicine_name = medicine_name.lower().strip()
    
    # Exact match
    if medicine_name in MEDICINES:
        return MEDICINES[medicine_name]
    
    # Partial match - try to find closest match
    matches = []
    for key, value in MEDICINES.items():
        if medicine_name in key or key in medicine_name or medicine_name in value["name"].lower():
            matches.append((key, value))
    
    if matches:
        # Return best match
        return matches[0][1]
    
    return None

def search_medicines(query):
    """Search for medicines by name"""
    if not query:
        return []
    
    query = query.lower().strip()
    results = []
    
    for key, value in MEDICINES.items():
        if query in key or query in value["name"].lower():
            results.append({
                "id": key,
                "name": value["name"],
                "uses": value["uses"][:3]  # First 3 uses
            })
    
    return results[:20]  # Return top 20 results

def get_all_medicines():
    """Get list of all available medicines"""
    all_medicines = []
    for key, value in MEDICINES.items():
        all_medicines.append({
            "id": key,
            "name": value["name"],
            "uses": value["uses"][:3]  # First 3 uses
        })
    return all_medicines

# Medicines count
MEDICINES_COUNT = len(MEDICINES)