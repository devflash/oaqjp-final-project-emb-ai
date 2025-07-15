from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def detect_emotion():
    textToAnalyze = request.args.get("textToAnalyze")

    result = emotion_detector(textToAnalyze)
    dominant_emotion = result["dominant_emotion"]
    return f"For the given statement, the system response is '{dominant_emotion}': {result}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

app.run(host="0.0.0.0", port=5000)