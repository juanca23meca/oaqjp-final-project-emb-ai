import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse or text_to_analyse.strip() == "":
        # Si el texto está vacío, devolvemos None en todas las emociones
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=myobj, headers=headers)
    status_code = response.status_code

    if status_code == 400:
        # Error 400 -> entrada en blanco o inválida
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response_data = response.json()
    emotions = response_data['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": dominant_emotion
    }

