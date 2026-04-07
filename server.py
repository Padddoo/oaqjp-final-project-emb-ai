from flask import Flask, render_template, request
from final_project.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Den Text aus der URL-Anfrage abgreifen
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Deine Funktion aufrufen
    response = emotion_detector(text_to_analyze)
    
    # Wenn die API einen Fehler liefert (Task 10 Vorbereitung)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Die Antwort für den User formatieren (laut Anleitung)
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)