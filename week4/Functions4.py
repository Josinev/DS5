import pandas as pd
import numpy as np
import langdetect as ld
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

#Function excercise 1
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

#Funcrtions excercise 2

#arrival_date_month een aantal keer geen maand
data = pd.read_excel('hotelBookings.xlsx')
def maakmaand(data):
    """Functie die De legen vlekken van de maanden opvult"""
    data.iloc[:847,4] = 'July'
    data.iloc[847:,4] = 'August'
    return data

#stay in week nights
def alsdaggeenintegerdrop(data):
    """Functie die afdwingt dat de nachten hele getallen zijn en anders een rij dropt"""
    data = data.drop(data.index[data['stays_in_week_nights'] == 4.3])
    data = data.reset_index(drop=True)
    return data

#adults aantal adults
def volwasseneonreeel(data):
    """Een onreeel aantal volwassenen wordt gedropt."""
    data = data.drop(data.index[data['adults'] >= (data.iloc[:,9].mean() * 2)])
    data = data.reset_index(drop=True)   
    return data

#adults aantal adults
def kinderenonreeel(data):
    """Een onreel aantal kinderen wordt gedropt"""
    data = data.drop(data.index[data['children'] >= (data.iloc[:,10].mean() * 2)])
    data = data.reset_index(drop=True)
    return data

#country moet een string van 3 letters zijn.
def landisstring(data):
    """Een landcode moet bestaan uit een string van 3 letters anders gedropt"""
    lst = data.iloc[:,13].unique().tolist()
    lst.remove(2)
    lst.remove(3)
    lst.remove(np.nan)

    data = data.drop(data.index[data['country'].isin(lst) == False])
    data = data.reset_index(drop=True)
    return data

#opschonen data hotelbookings
def opschonenhotelbookings(data):
    """Een functie die alle opschoon functiets uitvoert."""
    data = maakmaand(data)
    data = alsdaggeenintegerdrop(data)
    data = volwasseneonreeel(data)
    data = kinderenonreeel(data)
    data = landisstring(data)

    return data


#Function excercise 3
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
    return df1, df2, df3

#Function excercise 4.1
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

#Function excercise 4.2 Deel 1
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
    
#Function excercise 4.2 Deel 2
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
    
#Function excercise 4.2 Deel 3
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
 
    