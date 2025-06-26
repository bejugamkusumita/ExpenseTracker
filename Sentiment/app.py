from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = analyzer.polarity_scores(text)
    
    compound = sentiment['compound']
    neutral = sentiment['neu']
    positive = sentiment['pos']
    negative = sentiment['neg']

    if compound > 0:
        result = "😊 Positive Sentiment!"
        color = "#4CAF50"
    elif compound < 0:
        result = "☹️ Negative Sentiment!"
        color = "#f44336"
    else:
        result = "😐 Neutral Sentiment."
        color = "#2196F3"

    return render_template('result.html', 
                           text=text,
                           result=result, 
                           color=color,
                           positive=positive,
                           neutral=neutral,
                           negative=negative)
