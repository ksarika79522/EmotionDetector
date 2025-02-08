'''Deploy a Flask application that will allow a user to provide
a text string which will then be analyzed to determine which emotion amongst a set of 5
is the most likely emotion being conveyed by the given text.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion():
    '''Retrieve the provided text string from the user, then pass the text
    to be analyzed by the emotion detector. Finally, return a response displaying
    the confidence scores across all emotions and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear= response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant emotion']
    if dominant_emotion is None:
        return 'Invalid Text! Please Try Again'
    #the rest of the statement is shown to the right, sadness, and dominant emotion
    return f"""
        For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. 
        The dominant emotion is {dominant_emotion}."""


@app.route("/")
def render_index_page():
    '''
    Render the index page to the user, where the the text string 
    that is analyzed is provided and response is given back to the user.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    