import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import sklearn as sk
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
import seaborn as sns

#Exercise 3.1 Post-processing of predictions:
df_actual = pd.read_excel('training.xlsx')
df_prediction = pd.read_excel('predictions_training.xlsx')

df_actual['UOI'] = np.zeros(len(df_actual))
def UOI_cells(df_actual, df_prediction):
    sum_ = 0
    for i in range(0, len(df_actual)): 
        intersection = max([0, (min([df_actual.iloc[i,4], df_prediction.iloc[i,4]]) - max([df_actual.iloc[i,2], df_prediction.iloc[i,2]]))]) * max([0, (min([df_actual.iloc[i,5], df_prediction.iloc[i,5]]) - max([df_actual.iloc[i,3], df_prediction.iloc[i,3]]))])
        union = (df_actual.iloc[i,3] - df_actual.iloc[i,2]) * (df_actual.iloc[i,5] - df_actual.iloc[i,2]) + (df_prediction.iloc[i,3] - df_prediction.iloc[i,3]) * (df_prediction.iloc[i,5] - df_prediction.iloc[i,2])
        if intersection != 0:
            UOI = union / intersection
            df_actual.iloc[i,6] = UOI
            sum_+= UOI
    mean = sum_ / len(df_actual)
    return mean
print(UOI_cells(df_actual, df_prediction))

#Exercise 3.2 Fitting a model on the IOU:

#X = np.reshape(df_actual.iloc[:,1])
#Y = np.array(df_actual.iloc[:,6]).reshape(-1, 1)
#model = LogisticRegression()
#model.fit(X, Y)