import pandas as pd

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

print(dataopschonen(df))
