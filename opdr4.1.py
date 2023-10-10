import pandas as pd
import langdetect as ld

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
print(df)


