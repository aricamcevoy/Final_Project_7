import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = list(emotions.values())[0]
    disgust_score = list(emotions.values())[1]
    fear_score = list(emotions.values())[2]
    joy_score = list(emotions.values())[3]
    sadness_score = list(emotions.values())[4]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
    'anger': anger_score, 
    'disgust': disgust_score, 
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score, 
    'dominant emotion': dominant_emotion
    }
