from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    return f"La emoción dominante es {result['dominant_emotion'].capitalize()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
