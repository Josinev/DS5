import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import sklearn as sk
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
import seaborn as sns

# Exercise 1: Fitting a model
#a
np.random.seed(2)

x = np.random.uniform(0, 10, 200)
y = 2 * x**2 - 5 * x + 3 + np.random.normal(0, 10, 200)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset')
plt.show()

#b
inputvalues = {
    'y': y[:160],
    'x': x[:160]    
}
 
df_train = pd.DataFrame(inputvalues)

inputvalues = {
    'x': x[160:],
    'y': y[160:]
}

df_test = pd.DataFrame(inputvalues)

#c
#Second polynomial 

#d
df_train['x2'] = df_train['x']**2
X = sm.add_constant(df_train.iloc[:,1:3])
model = sm.OLS(df_train['y'], X)
results = model.fit()

predict_train_y = results.predict(X)

plt.scatter(df_train['x'], df_train['y'])
plt.scatter(df_train['x'], predict_train_y, color = 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Regression Model (Degree 2)')
plt.show()

#e
R2 = results.rsquared
mse = mean_squared_error(df_train['y'], predict_train_y)
print(R2, mse)

df_test['x2'] = df_test['x']**2
X = sm.add_constant(df_test.iloc[:,1:3])
model = sm.OLS(df_test['y'], X)
results = model.fit()
predict_test_y = results.predict(X)
R2 = results.rsquared
mse = mean_squared_error(df_test['y'], predict_test_y)
print(R2, mse)
#f
#The R2 of the test sample is lower than the training sample. The MSE of the test sample is way lower than the training sample which is also positive
#This means that the model is good in predicing.