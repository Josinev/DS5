import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import sklearn as sk
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
import seaborn as sns

#Data outlier functions:
def volatile_acidity_drops(df):
    """If a volatile acidity is more than 3 times the median we drop the row."""
    df = df.drop(df.index[df.iloc[:,1] >= df.iloc[:,1].median() * 3])
    return df

def total_sulfur_dioxide_drops(df):
    """If a total sulfur dioxide is more than 4 times the median we drop the row."""
    df = df.drop(df.index[df.iloc[:,6] >= df.iloc[:,6].median() * 4])
    return df

def density_drops(df):
    """If a density is more than 3 times the median we drop the row."""
    df = df.drop(df.index[df.iloc[:,7] >= df.iloc[:,7].median() * 1.1])
    return df

def sulphates_drops(df):
    """If the amount of sulphates is more than 3 times the median we drop the row."""
    df = df.drop(df.index[df.iloc[:,10] >= df.iloc[:,10].median() * 3])
    return df

def outlier_drops(df):
    """Function that all the columns checks for outliers and deletes these."""
    df = volatile_acidity_drops(df)
    df = total_sulfur_dioxide_drops(df)
    df = density_drops(df)
    df = sulphates_drops(df)
    df = df.reset_index()
    return df


#Exercise 2: Predicting the quality of wine
#a 
df = pd.read_excel('winequality-red.xlsx')

#b
#check

#c
df = outlier_drops(df)
#there are no missing values

#d ?
#sns.pairplot(df)
#plt.show()
    
#e
df_training_x = df.iloc[:int(len(df)*0.8), :12]
df_training_y = df.iloc[:int(len(df)*0.8), 12]

df_test_x = df.iloc[int(len(df)*0.8):, :12]
df_test_y = df.iloc[int(len(df)*0.8):, 12]

#f
X = sm.add_constant(df_training_x)
model = sm.OLS(df_training_y, X)
results = model.fit()
predict_training_y = results.predict(X)

#g
R2 = results.rsquared
print(R2)

X = sm.add_constant(df_test_x)
model = sm.OLS(df_test_y, X)
results = model.fit()
predict_test_y = results.predict(X)
R2 = results.rsquared
print(R2)

#i
