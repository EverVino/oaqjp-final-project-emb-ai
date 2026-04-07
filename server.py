''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as em

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using sentiment_analysis()
        function. The output returned shows emotion related with the 
        text
    '''
    text_to_analyse = request.args.get("textToAnalyze")
    res = em(text_to_analyse)
    if res["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return res

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
