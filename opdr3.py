import pandas as pd

def data_analysis(df = pd.DataFrame):
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
data_analysis(df)