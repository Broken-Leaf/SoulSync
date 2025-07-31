# health_tips.py
from core.dict import symptom_health_tips

def get_health_tips(user_symptoms):
    tips = []
    for s in user_symptoms:
        s = s.strip().lower()
        for key in symptom_health_tips:
            if key in s:
                tips.append(symptom_health_tips[key])
                break
    return tips if tips else ["Take care and rest well. Consult a doctor if symptoms worsen."]
