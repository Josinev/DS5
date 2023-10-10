from textblob import TextBlob
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import langdetect as ld


#opdr 4.1
df = pd.read_excel('tweets.xlsx') 
def opdr41(df):
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

#tweet = df.iloc[4,3]
#print(tweet)
#print(analyze_sentiment_english(tweet))
    
#opdr 4.2 deel 2
def analyze_sentiment_other(df):
    """functie die polarity van de tweet berekend en daarna het sentiment retourneert"""
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(df)
    compound_score = scores["compound"]
    
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"
    
#opdr 4.2 deel 3
def sentiment(df):
    opdr41(df)
    senti = []
    for i in range(len(df)):
        if df.iloc[i,9] == "en":
           a =  analyze_sentiment_english(df)
           senti.append(a)
        else:
         b = analyze_sentiment_other(df)
         senti.append(b)
    df["Sentiment"] = senti
    return df

