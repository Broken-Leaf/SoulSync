disease_data = {
    "diabetes": ["increased thirst", "frequent urination", "extreme hunger", "fatigue", "blurred vision"],
    "hypertension": ["headache", "shortness of breath", "nosebleeds", "chest pain", "dizziness"],
    "asthma": ["wheezing", "coughing", "shortness of breath", "chest tightness"],
    "flu": ["fever", "chills", "muscle aches", "cough", "congestion", "runny nose"],
    "covid-19": ["fever", "dry cough", "tiredness", "loss of taste", "difficulty breathing"],
    "anemia": ["fatigue", "weakness", "pale skin", "shortness of breath", "dizziness"],
    "migraine": ["throbbing pain", "sensitivity to light", "nausea", "vomiting", "blurred vision"],
    "tuberculosis": ["persistent cough", "fever", "night sweats", "weight loss", "fatigue"],
    "pneumonia": ["chest pain", "cough with phlegm", "fever", "difficulty breathing", "chills"],
    "arthritis": ["joint pain", "stiffness", "swelling", "reduced motion", "fatigue"],
    "malaria": ["fever", "chills", "sweating", "nausea", "vomiting"],
    "dengue": ["high fever", "headache", "rash", "pain behind eyes", "joint pain"],
    "typhoid": ["prolonged fever", "abdominal pain", "weakness", "loss of appetite", "constipation"],
    "ulcer": ["stomach pain", "bloating", "heartburn", "nausea", "indigestion"],
    "hepatitis": ["jaundice", "fatigue", "abdominal pain", "nausea", "loss of appetite"],
    "jaundice": ["yellow skin", "yellow eyes", "dark urine", "fatigue", "abdominal pain"],
    "chikungunya": ["joint pain", "fever", "rash", "muscle pain", "swelling"],
    "UTI": ["burning urination", "frequent urination", "pelvic pain", "cloudy urine", "strong smell"],
    "kidney stones": ["sharp back pain", "blood in urine", "nausea", "vomiting", "painful urination"],
    "gallstones": ["abdominal pain", "nausea", "vomiting", "indigestion", "jaundice"],
    "thyroid disorder": ["fatigue", "weight gain", "cold sensitivity", "dry skin", "depression"],
    "depression": ["sadness", "loss of interest", "fatigue", "insomnia", "feelings of guilt"],
    "anxiety": ["restlessness", "rapid heartbeat", "sweating", "trouble concentrating", "irritability"],
    "sinusitis": ["facial pain", "nasal congestion", "runny nose", "headache", "fever"],
    "eczema": ["itching", "dry skin", "red patches", "cracking", "swelling"],
    "psoriasis": ["scaly skin", "itching", "red patches", "dry skin", "painful joints"],
    "bronchitis": ["cough with mucus", "fatigue", "shortness of breath", "chest discomfort", "fever"],
    "measles": ["rash", "fever", "cough", "runny nose", "red eyes"],
    "chickenpox": ["itchy rash", "fever", "tiredness", "loss of appetite", "headache"],
    "mumps": ["swollen cheeks", "fever", "headache", "muscle aches", "fatigue"],
    "tonsillitis": ["sore throat", "fever", "swollen tonsils", "difficulty swallowing", "ear pain"],
    "appendicitis": ["abdominal pain", "nausea", "vomiting", "loss of appetite", "fever"],
    "gastroenteritis": ["diarrhea", "vomiting", "abdominal cramps", "fever", "nausea"],
    "constipation": ["hard stools", "infrequent stools", "straining", "bloating", "abdominal discomfort"],
    "acne": ["pimples", "blackheads", "whiteheads", "oily skin", "scarring"],
    "obesity": ["excess weight", "breathlessness", "joint pain", "fatigue", "snoring"],
    "vitamin D deficiency": ["bone pain", "muscle weakness", "fatigue", "mood changes", "hair loss"],
    "osteoporosis": ["back pain", "stooped posture", "fractures", "loss of height", "bone weakness"],
    "scabies": ["intense itching", "rash", "blisters", "thin burrow lines", "skin sores"],
    "allergy": ["sneezing", "itchy eyes", "runny nose", "rash", "swelling"]
}

symptom_health_tips = {
    "fever": [
        "Drink plenty of fluids to stay hydrated.",
        "Take adequate rest and avoid exertion."
    ],
    "chills": [
        "Keep yourself warm with a blanket.",
        "Drink warm fluids like soups and herbal tea."
    ],
    "muscle aches": [
        "Gently stretch and rest the muscles.",
        "Apply warm compress to relieve pain."
    ],
    "cough": [
        "Use warm water and steam inhalation to soothe your throat.",
        "Avoid cold drinks and dusty environments."
    ],
    "congestion": [
        "Inhale steam to relieve nasal congestion.",
        "Use saline nasal spray."
    ],
    "runny nose": [
        "Use tissues and wash hands frequently.",
        "Stay away from allergens and keep warm."
    ],
    "dry cough": [
        "Suck lozenges to soothe the throat.",
        "Keep a humidifier nearby to moisten the air."
    ],
    "loss of taste": [
        "Try sour foods like lemon to stimulate taste buds.",
        "Stay hydrated and maintain oral hygiene."
    ],
    "difficulty breathing": [
        "Avoid physical exertion.",
        "Sit upright and try breathing exercises."
    ],
    "fatigue": [
        "Take short naps and avoid overexertion.",
        "Eat nutritious meals at regular intervals."
    ],
    "joint pain": [
        "Apply warm compress and rest the joint.",
        "Do gentle stretching or consult a physiotherapist."
    ],
    "swelling": [
        "Elevate the affected area.",
        "Apply cold compress to reduce inflammation."
    ],
    "headache": [
        "Rest in a quiet, dark room.",
        "Avoid screen time and drink enough water."
    ],
    "rash": [
        "Keep the area clean and dry.",
        "Avoid scratching and use gentle moisturizers."
    ],
    "nausea": [
        "Eat small, bland meals like toast or banana.",
        "Sip on clear fluids or ginger tea."
    ],
    "vomiting": [
        "Take sips of ORS or electrolyte drinks.",
        "Avoid solid foods until vomiting stops."
    ],
    "diarrhea": [
        "Drink ORS and eat a BRAT diet (banana, rice, apple, toast).",
        "Avoid dairy and greasy food."
    ],
    "sore throat": [
        "Gargle with warm salt water.",
        "Drink warm teas with honey."
    ],
    "shortness of breath": [
        "Practice deep breathing exercises.",
        "Avoid smoke, dust, and allergens."
    ],
    "itching": [
        "Use anti-itch cream or calamine lotion.",
        "Avoid hot showers and harsh soaps."
    ],
    "blurred vision": [
        "Rest your eyes and avoid bright screens.",
        "See a doctor if it persists."
    ],
    "abdominal pain": [
        "Avoid spicy foods and eat light meals.",
        "Use a heating pad for comfort."
    ],
    "pale skin": [
        "Increase iron-rich foods like spinach and beans.",
        "Get your hemoglobin levels checked."
    ],
    "weight gain": [
        "Limit sugary foods and exercise regularly.",
        "Monitor calorie intake."
    ],
    "cold sensitivity": [
        "Wear layered clothing.",
        "Use hot water bottles in cold weather."
    ],
    "depression": [
        "Talk to someone you trust.",
        "Maintain a routine and get sunlight."
    ],
    "anxiety": [
        "Practice deep breathing and mindfulness.",
        "Limit caffeine and avoid overthinking."
    ],
    "insomnia": [
        "Avoid screens before bed.",
        "Maintain a regular sleep schedule."
    ],
    "loss of appetite": [
        "Eat small meals more frequently.",
        "Try bitter foods like lemon to stimulate appetite."
    ]
}