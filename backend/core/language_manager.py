import requests

def translate(text, target_lang):
    if target_lang == "en":
        return text

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": target_lang,
        "dt": "t",
        "q": text
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            result = response.json()
            return result[0][0][0]
        else:
            return text
    except:
        return text

def detect_language(text):
    # Very basic detection: if Devanagari characters present, assume Hindi
    for char in text:
        if '\u0900' <= char <= '\u097F':
            return "hi"
    return "en"