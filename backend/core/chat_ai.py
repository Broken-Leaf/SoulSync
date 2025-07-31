import json
import requests
import re
import os
from datetime import datetime
from collections import defaultdict
from .load_env import load_env_file
from datetime import datetime

# Load env
load_env_file()

# Paths
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_LOG_PATH = os.path.join(CURRENT_DIR, "memory_log.txt")
CONVERSATION_HISTORY_PATH = os.path.join(CURRENT_DIR, "conversation_history.json")
MEDICINE_RECOMMENDATIONS_PATH = os.path.join(CURRENT_DIR, "medicine_recommendations.json")

# 🧠 Memory Functions
def save_to_memory(user_input, ai_response):
    with open(MEMORY_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"User: {user_input.strip()}\nAI: {ai_response.strip()}\n\n")
    try:
        if os.path.exists(CONVERSATION_HISTORY_PATH):
            with open(CONVERSATION_HISTORY_PATH, "r", encoding="utf-8") as f:
                history = json.load(f)
        else:
            history = []
        history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input.strip(),
            "ai": ai_response.strip()
        })
        if len(history) > 50:
            history = history[-50:]
        with open(CONVERSATION_HISTORY_PATH, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        print(f"Error saving memory: {e}")

def get_recent_memory():
    try:
        if os.path.exists(CONVERSATION_HISTORY_PATH):
            with open(CONVERSATION_HISTORY_PATH, "r", encoding="utf-8") as f:
                history = json.load(f)
            return "\n\n".join([f"User: {h['user']}\nAI: {h['ai']}" for h in history[-10:]])
        return ""
    except Exception as e:
        print(f"Memory read error: {e}")
        return ""

def check_for_time_request(user_input):
    keywords = ["current time", "what time", "what is the time", "what is the time now", "tell me time"]
    return any(k in user_input.lower() for k in keywords)

def get_indian_time():
    import pytz
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist).strftime("%I:%M %p")

# 🧠 Combined: AI + Context in 1 call
def call_ai_with_context(prompt, memory_context, max_tokens=300):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY', '')}",
        "Content-Type": "application/json"
    }

    system_prompt = """
You are SoulSync AI. First, understand the user's intent and determine if it's:
[CONTEXT]: medical, emotional, or general

Then reply accordingly:
- For medical: behave like a knowledgeable Indian health assistant. Give trustworthy advice on common conditions. Suggest safe OTC Indian medicines (e.g., Cipla, Dabur, Himalaya), proper dosage (if safe), common side effects, and always end with a friendly reminder to consult a doctor. Use clear, simple, human-like responses. Never pretend to be a doctor. Be careful, warm, and helpful.
- For emotional: speak like a caring Indian friend. Be comforting and sincere, not robotic. Use natural tone and warm, supportive responses.
- For general: keep replies short, friendly, and culturally familiar — like a smart Indian buddy. Be direct and useful.

Strict Greeting Rules:
- Greet **only** if the user message is **exactly** “hi” or “hello” (case-insensitive). Only these two.
- In that case, greet once using **only "Namaste😊"**. Never greet with “hi”, “hello”, “hey” or anything else.
- If the user says anything else (like “hmm”, “okay”, “story”, “good morning”), **do not greet** at all.
- Do not repeat “Namaste” again during the same conversation.

Always reply in a way that sounds natural, local (India), and human — not like a machine. Keep responses short and meaningful. Avoid generic or robotic phrases. Never say you're an AI unless asked.

At the end, include the tag: [CONTEXT: medical] / [CONTEXT: emotional] / [CONTEXT: general]

"""

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": system_prompt.strip()},
            {"role": "system", "content": f"Memory:\n{memory_context.strip()}"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()["choices"][0]["message"]["content"]

        # Extract context
        match = re.search(r"\[CONTEXT:\s*(\w+)\s*\]", data)
        context = match.group(1).lower() if match else "general"
        clean_reply = data.replace(match.group(0), "").strip() if match else data

        return clean_reply, context
    except Exception as e:
        print("AI error:", e)
        return "Sorry, I'm not able to help at this moment 🤕", "general"

# 💊 Medicine Extraction
def extract_medicine_recommendations(ai_response):
    extraction_prompt = f"""
Extract symptom and medicine recommendations in this format:
{{
  "symptom": "flu",
  "medications": [
    {{
      "name": "Paracetamol",
      "dosage": "500mg after food",
      "notes": "Can cause nausea"
    }}
  ]
}}

Response:
\"\"\"{ai_response}\"\"\"
"""

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "Extract clean JSON from AI response"},
            {"role": "user", "content": extraction_prompt}
        ],
        "temperature": 0.0,
        "max_tokens": 500
    }

    try:
        res = requests.post(url, json=payload, headers=headers)
        raw = res.json()["choices"][0]["message"]["content"]
        json_str = raw.replace("```json", "").replace("```", "").strip()
        data = json.loads(json_str)
        if "symptom" in data and "medications" in data:
            save_medicine_recommendation(data["symptom"], data["medications"])
        return data
    except Exception as e:
        print("Medicine parse error:", e)
        return {}

# 📅 Save by date

def save_medicine_recommendation(symptom, medications):
    date_key = datetime.now().strftime("%d %b %Y")  # e.g., "09 Jul 2025"
    entry = {
        "name": symptom,
        "medications": medications,
        "timestamp": datetime.now().isoformat()
    }

    # Load file
    if os.path.exists(MEDICINE_RECOMMENDATIONS_PATH):
        with open(MEDICINE_RECOMMENDATIONS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    if date_key not in data:
        data[date_key] = []

    data[date_key].append(entry)

    with open(MEDICINE_RECOMMENDATIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# ✨ ENTRY POINT: General Reply
def generate_general_reply(user_input):
    memory_context = get_recent_memory()

    if check_for_time_request(user_input):
        return f"The current Indian time is {get_indian_time()} 🕒"

    reply, context_type = call_ai_with_context(user_input, memory_context)

    if context_type == "medical":
        extract_medicine_recommendations(reply)

    save_to_memory(user_input, reply)
    return reply

# 🩺 Manual Doctor Override
def call_grok_api_with_medicine_suggestion(prompt):
    full_prompt = prompt + "\n\nGive:\n1. Short explanation\n2. OTC Indian meds\n3. Side effects\n4. Senior-safe dose\n5. Doctor consult warning"
    reply, _ = call_ai_with_context(full_prompt, get_recent_memory(), max_tokens=500)
    extract_medicine_recommendations(reply)
    return reply