import pandas as pd

df = pd.read_excel('detailedRetail.xlsx')

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()

#Total sales for each category
df1['total_sales_category']= df.groupby('Category').sum('Sales')
df1['total_sales_category_percent'] = (df1['total_sales_category'] / df1['total_sales_category'].sum()) * 100

df2['total_sales_month']= df.groupby('Month').sum('Sales')
df2['total_sales_month_percent'] = (df2['total_sales_month'] / df2['total_sales_month'].sum()) * 100

df3['sales_manager'] = df.groupby('Sales Manager').sum('Sales')
df3['sales_manager_percent'] = (df3['sales_manager']/ df3['sales_manager'].sum()) * 100

dfs = pd.merge(df1, df2, df3)
print(dfs)
#dfs.to_excel('reportRetail.xlsx')