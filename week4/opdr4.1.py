import pandas as pd
import langdetect as ld

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader')

df = pd.read_excel('tweets.xlsx') 
def opdr41(df):
    """Functie die een nieuwe colom genaamd language maakt, waar de taal van de tweet in staat."""
    code = []
    for i in range(len(df)):
        try:
            taal = ld.detect(df.iloc[i,3])
            code.append(taal)
        except:
            taal = 'unknown'
            code.append(taal)

    df['Language'] = code
    return df


def analyze_sentiment_other(df):
    """functie die polarity van de tweet berekend en daarna het sentiment retourneert"""
    score = SentimentIntensityAnalyzer().polarity_scores(tweet)
    compound_score = score["compound"]
    
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"
    

tweet = df.iloc[4,3]
print(tweet)
print(analyze_sentiment_other(tweet))