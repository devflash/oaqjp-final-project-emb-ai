import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    input = { "raw_document": { "text": text_to_analyse } }

    if text_to_analyse == '':
        return {'anger': 'None','disgust': 'None','fear': 'None','joy': 'None','sadness': 'None','dominant_emotion': 'None'}

    result = requests.post(url, json=input, headers=headers)
 
    if result.status_code == 200:
        formatted_result = json.loads(result.text)
        emotions = formatted_result["emotionPredictions"][0]["emotion"]
        result = {}
        max_score = 0
        dominant_emotion = 'None'
        for e,s in emotions.items():
            if s > max_score:
                max_score = s
                dominant_emotion = e
            result[e] = s
        result['dominant_emotion'] = dominant_emotion
        return result
    
    if result.status_code == 400:
        return {'anger': 'None','disgust': 'None','fear': 'None','joy': 'None','sadness': 'None','dominant_emotion': 'None'}
    