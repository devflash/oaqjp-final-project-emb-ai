'''Emotion detector server'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def detect_emotion():
    '''Function that calls emotion_detector'''
    text_to_analyse = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyse)
    dominant_emotion = result["dominant_emotion"]
    if dominant_emotion == 'None':
        return 'Invalid text! Please try again!.'

    return f"For the given statement, the system response is '{dominant_emotion}': {result}"

@app.route("/")
def render_index_page():
    '''Function that renders HTML'''
    return render_template('index.html')

app.run(host="0.0.0.0", port=5001)
