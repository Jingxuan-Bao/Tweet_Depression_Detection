from flask import Flask, request, jsonify
import joblib
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

import re
import string
import nltk
import contractions
nltk.download('stopwords')
from flask import Flask, jsonify
from flask_cors import CORS

def remove_emojis(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def preprocess_tweet_text(tweet_text):
    # Conver to string
    tweet_text = str(tweet_text)

    # Convert to lowercase
    tweet_text = tweet_text.lower()

    # Expand contractions
    tweet_text = contractions.fix(tweet_text)

    # Remove URLs
    tweet_text = re.sub(r"http\S+", "", tweet_text)

    # Remove mentions (@) and hashtags (#)
    tweet_text = re.sub(r'\@\w+|\#', '', tweet_text)

    # Remove emojis
    tweet_text = remove_emojis(tweet_text)

    # Remove punctuation
    tweet_text = tweet_text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    tweet_text = re.sub(r"\d+", "", tweet_text)

    # Remove whitespace
    tweet_text = tweet_text.strip()

    # Tokenize the text into individual words
    tweet_words = tweet_text.split()

    # Remove stop words using NLTK library
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tweet_words = [word for word in tweet_words if word not in stop_words]

    # Join the remaining words back into a string
    processed_tweet_text = " ".join(tweet_words)

    return processed_tweet_text

app = Flask(__name__)
CORS(app)

# Load the saved SVM model
svm_model = joblib.load('../models/svm_model.pkl')

# Load the saved TfidfVectorizer
tfidf_vectorizer = joblib.load('../models/tfidf_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input tweet
    data = request.get_json(force=True)
    tweet = data['tweet']

    tweet = preprocess_tweet_text(tweet)
    print('Input tweet : ', tweet)
    # Preprocess and transform the input tweet using the saved TfidfVectorizer
    tweet_tfidf = tfidf_vectorizer.transform([tweet])
    print('tweet tfidf : ', tweet_tfidf)
    # Make a prediction using the saved SVM model
    prediction = svm_model.predict(tweet_tfidf)
    #prediction_prob = svm_model.predict_proba(tweet_tfidf)

    print('Prediction results : ', prediction)
    # Return the result as JSON
    return jsonify({
        'prediction': int(prediction[0])
    })

if __name__ == '__main__':
    app.run(port=8080)
