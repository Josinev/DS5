from textblob import TextBlob
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import langdetect as ld
import numpy as np
import nltk
nltk.download('vader')

#opgave 1
df = pd.read_excel("dataProject4.xlsx", sheet_name="20000-211000")
def dataopschonen(df):
    """Functie waarin de data van project 4 wordt opgeschoond. 
    De kolomnamen worden benoemd, de eerste vier rijen, de dubbele rijen worden verwijderd. 
    Ook wordt alle tekst omgezet naar kleine letters en wordt er een gemiddelde kolom over de aantal jaren toegevoegd
    input een dataframe
    output datzelfde dataframe maar dan opgeschoond
    """

    df.columns=('Customer number', 'Postal Code', 'Customer Classification (CRM)', 'Horeca menu webshop', 'Prd. name Webshop','Brand name', 'Contents', '2018','2019','2020','2021','2022') #kolomnamen
    df = df.drop(df.index[0:4])#verwijderd de eerste 4 rijen
    df.drop(index = df[df.iloc[:, 2] == 'Result'].index, inplace = True) #verwijderd alle result rijen
    df.drop_duplicates(inplace = True) #verwijderd alle dubbele rijen
    
    df.reset_index(drop = True, inplace = True) #herstelt de index 
    
    df["Postal Code"] = df["Postal Code"].str.lower()
    df["Customer Classification (CRM)"] = df["Customer Classification (CRM)"].str.lower()
    df['Horeca menu webshop'] = df['Horeca menu webshop'].str.lower()
    df['Prd. name Webshop'] = df['Prd. name Webshop'].str.lower()
    df['Brand name'] = df['Brand name'].str.lower()
    df['Total mean']=df.iloc[:, 7:12].mean(axis=1) #voegt de kolom "Total mean" toe
    return df 

#opgave 2
#arrival_date_month een aantal keer geen maand
data.iloc[:847,4] = 'July'
data.iloc[847:,4] = 'August'
print(len(data))

#stay in week nights
data = data.drop(data.index[data['stays_in_week_nights'] == 4.3])
data = data.reset_index(drop=True)
print(len(data))

#adults aantal adults
data = data.drop(data.index[data['adults'] >= (data.iloc[:,9].mean() * 2)])
data = data.reset_index(drop=True)   
print(len(data))

#adults aantal adults
data = data.drop(data.index[data['children'] >= (data.iloc[:,10].mean() * 2)])
data = data.reset_index(drop=True)
print(len(data))

#country moet een string van 3 letters zijn.
lst = data.iloc[:,13].unique().tolist()
lst.remove(2)
lst.remove(3)
lst.remove(np.nan)

data = data.drop(data.index[data['country'].isin(lst) == False])
data = data.reset_index(drop=True)
print(len(data))

#opdracht 3
def data_analysis(df = pd.DataFrame):
    '''Rekent verschillende waardes van dataframe uit.
    Input: Dataframe
    Output: Nieuwe DataFrame genaamd reportRetail met daarin verschillende berekende waardes'''
    #Creert nieuwe DataFrame
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()

    #Berekent de totale sales voor elke category
    df1['total_sales_category']= df.groupby('Category').sum('Sales')
    #Berekent het percentage van totale sales voor elke category
    df1['total_sales_category_percent'] = (df1['total_sales_category'] / df1['total_sales_category'].sum()) * 100

    #Berekent de verkopen voor elke maand
    df2['total_sales_month']= df.groupby('Month').sum('Sales')
    #Berekent het percentage van verkopen per maand
    df2['total_sales_month_percent'] = (df2['total_sales_month'] / df2['total_sales_month'].sum()) * 100

    #Berekent de sales per manager
    df3['sales_manager'] = df.groupby('Sales Manager').sum('Sales')
    #Berekent het percentage van de sales per manager
    df3['sales_manager_percent'] = (df3['sales_manager']/ df3['sales_manager'].sum()) * 100

    #Voegt de 3 verschillende datasets bij elkaar
    result = pd.concat([df1, df2, df3])
    #Zet de dataframe om in een excel bestand
    result.to_excel('reportRetail.xlsx')


df = pd.read_excel('detailedRetail.xlsx')

#opdracht 4.1
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
    
    #opdr 4.2 deel 1
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
def sentiment(df):
    opdr41(df)
    senti = []
    for i in range(len(df)):
        if df.iloc[i,9] == "en":
           a =  analyze_sentiment_english(df.iloc[i,3])
           senti.append(a)
        else:
         b = analyze_sentiment_other(df.iloc[i,3])
         senti.append(b)
    df["Sentiment"] = senti
    return df