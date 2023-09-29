import pandas as pd
df = pd.read_excel("dataProject4.xlsx", sheet_name="20000-211000")

df.columns=('Customer number', 'Postal Code', 'Customer Classification (CRM)', 'Horeca menu webshop', 'Prd. name Webschop','Brand name', 'Contents', '2018','2019','2020','2021','2022')
df = df.drop(df.index[0:4])
df.drop(index = df[df.iloc[:, 2] == 'Result'].index, inplace = True)
df.drop_duplicates(inplace = True) 

df.reset_index(drop = True, inplace = True)
print(df.info()) 
#print(len(df))
