from textblob import TextBlob
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

#opdr 4.2 deel 1
tweet = pd.read_excel('tweets.xlsx')
def analyze_sentiment_english(tweet):
    """functie die van een tweet een textblob maakt een daarna het sentiment van de tweet retourneert"""
    blob = TextBlob(tweet)
    polarity_score = blob.sentiment.polarity
    
    if polarity_score > 0:
        return "positive"
    elif polarity_score < 0:
        return "negative"
    else:
        return "neutural"
    
#opdr 4.2 deel 2
def analyze_sentiment_other(tweet):
    """functie die polarity van de tweet berekend en daarna het sentiment retourneert"""
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(tweet)
    compound_score = scores["compound"]
    
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"
    
#opdr 4.2 deel 3
tweet['sentiment'] = tweet.apply(apply_sentiment_analysis, axis=1)
    

    
    
    
    