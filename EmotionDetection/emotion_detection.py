import requests
import json

def emotion_detector(text_to_analyze):
    # URL del servicio Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados requeridos
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Cuerpo de la solicitud
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Enviar solicitud POST
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convertir la respuesta JSON en diccionario
    formatted_response = json.loads(response.text)
    
    # Extraer el bloque de emociones
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    
    # Encontrar la emoción dominante (la de puntuación más alta)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Crear el diccionario de salida con el formato solicitado
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result
