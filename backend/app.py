from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from core.language_manager import detect_language, translate
from core.chat_ai import generate_general_reply
from core.doctor_consult import analyze_symptoms_stage2

app = Flask(__name__)
CORS(app)

MEDICINE_RECOMMENDATIONS_PATH = os.path.join(os.getcwd(), "medicine_recommendations.json")

@app.route("/get_medicine_recommendations", methods=["GET"])
def get_medicine_recommendations():
    if os.path.exists(MEDICINE_RECOMMENDATIONS_PATH):
        return send_from_directory(
            directory=os.path.dirname(MEDICINE_RECOMMENDATIONS_PATH),
            path=os.path.basename(MEDICINE_RECOMMENDATIONS_PATH),
            as_attachment=False
        )
    else:
        return jsonify({"error": "Medicine recommendations file not found"}), 404


@app.route("/ai/chat", methods=["POST"])
def ai_chat():
    try:
        data = request.get_json(force=True)
        user_input = data.get("input", "").strip()
        user_answers = data.get("follow_up_answers", [])
        possible_disease = data.get("possible_disease")
    except Exception as e:
        print("Error in /ai/chat:", e)
        return jsonify({"error": str(e)}), 500

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    user_lang = detect_language(user_input)
    translated_input = translate(user_input, "en")

    if user_answers and possible_disease:
        diagnosis = analyze_symptoms_stage2(user_answers, possible_disease)
        reply = (
            diagnosis["advice"][user_lang]
            if diagnosis["status"] == "diagnosis"
            else diagnosis["message"][user_lang]
        )
        return jsonify({
            "input_language": user_lang,
            "translated_input": translated_input,
            "reply": translate(reply, user_lang),
            "disease_analysis": diagnosis
        })

    reply = generate_general_reply(translated_input)

    return jsonify({
        "input_language": user_lang,
        "translated_input": translated_input,
        "reply": translate(reply, user_lang),
        "disease_analysis": {}
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)