import re
from difflib import SequenceMatcher
from core.health_tips import get_health_tips
from core.dict import disease_data

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s,]', '', text)
    return text

def match_symptoms(user_symptoms, disease_symptoms):
    matches = 0
    for us in user_symptoms:
        for ds in disease_symptoms:
            score = SequenceMatcher(None, us.strip(), ds).ratio()
            if score > 0.5:
                matches += 1
                break
    return matches

def analyze_symptoms_stage1(user_input):
    user_input = preprocess(user_input)
    user_symptoms = [sym.strip() for sym in user_input.split(',')]
    disease_scores = {}

    for disease, symptoms in disease_data.items():
        matches = match_symptoms(user_symptoms, symptoms)
        if matches:
            disease_scores[disease] = matches

    if not disease_scores:
        return {"status": "ask_more", "message": "Please tell me more symptoms to understand better."}

    top_disease = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)[0][0]
    follow_ups = disease_data[top_disease]
    tips = get_health_tips(user_symptoms)

    return {
        "status": "follow_up",
        "possible_disease": top_disease,
        "follow_up_questions": follow_ups,
        "health_tips": tips
    }

def analyze_symptoms_stage2(user_answers, possible_disease):
    user_answers = [preprocess(ans) for ans in user_answers]
    expected_symptoms = disease_data.get(possible_disease, [])
    match_count = match_symptoms(user_answers, expected_symptoms)
    required = max(2, len(expected_symptoms) // 3)

    if match_count >= required:
        return {
            "status": "diagnosis",
            "disease": possible_disease,
            "advice": {
                "en": f"These symptoms suggest {possible_disease}. Consult a doctor. Rest and stay safe.",
                "hi": f"ये लक्षण {possible_disease} की ओर इशारा करते हैं। कृपया चिकित्सक से संपर्क करें।"
            }
        }
    else:
        return {
            "status": "uncertain",
            "message": {
                "en": "The symptoms are not sufficient to confirm any disease. Please consult a doctor.",
                "hi": "लक्षण पर्याप्त नहीं हैं। कृपया डॉक्टर से सलाह लें।"
            }
        }