import pandas as pd
import langdetect as ld

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

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

print(opdr41(df))