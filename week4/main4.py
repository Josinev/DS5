import pandas as pd

from Functions4 import dataopschonen
from Functions4 import opschonenhotelbookings
from Functions4 import data_analysis
from Functions4 import opdr41
from Functions4 import analyze_sentiment_english
from Functions4 import analyze_sentiment_other
from Functions4 import sentiment

df1 = pd.read_excel("dataProject4.xlsx", sheet_name="20000-211000")
df2 = pd.read_excel('hotelBookings.xlsx')
df3 = pd.read_excel('detailedRetail.xlsx')
df4 = pd.read_excel('tweets.xlsx') 

# Exercise 1 
#print(dataopschonen(df1))                                  Werkt duur even

# Exercise 2
#print(opschonenhotelbookings(df2))                         Werkt duur even

# Exercise 3
#print(data_analysis(df3))                                  Werkt duur even

# Exercise 4.1
#print(opdr41(df4))                                         Werkt duur lang

# Exercise 4.2 deel 1
#print(analyze_sentiment_english(df4.iloc[2,3]))            Werkt duur even
#print(analyze_sentiment_english(df4.iloc[3,3]))

# Exercise 4.2 deel 2
#print(analyze_sentiment_other(df4.iloc[3,3]))              Werkt niet, maar er is een poging gewaagt

#Exercise 4.2 deel 3
#print(sentiment(opdr41(df4)))                              Werkt niet, maar er is een poging gewaagt