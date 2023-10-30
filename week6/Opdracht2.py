import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

#a.
df = pd.read_excel('winequality-red.xlsx')

#b.
#gedaan

#c.
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

df = outlier_drops(df)

#d.
plt.figure(figsize = (8,6))
#sns.pairplot(df)
#plt.show()

#e.
X = df.drop("quality", axis=1)
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#f.
X = sm.add_constant(X_train)
model = sm.OLS(y_train, X)