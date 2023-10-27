import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
from sklearn.metrics import r2_score

np.random.seed(2)

x = np.random.uniform(0, 10, 200)
y = 2 * x**2 - 5 * x + 3 + np.random.normal(0, 10, 200)

# Plot the dataset
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset')
#plt.show()

#b.
inputValuesTrain = {
    'x' : x[:160],
    'y' : y[:160]
}
data_train = pd.DataFrame(inputValuesTrain)

inputValuesTest = {
    'x' : x[160:],
    'y' : y[160:]
}

data_test= pd.DataFrame(inputValuesTest)

#c.
#Kwadratische vergelijking

#d.
train_x = data_train['x']
train_x_sq = pd.DataFrame(data_train['x']**2)

train_x_poly = pd.concat([train_x, train_x_sq], axis=1)

X = sm.add_constant(train_x_sq)
model = sm.OLS(data_train['y'], X)
results = model.fit()

predicted_train_y = results.predict(X)
plt.scatter(data_train['x'], data_train['y'])
plt.scatter(data_train['x'], predicted_train_y, color='red')
#plt.show()
#e.
r_squared = results.rsquared
print(r_squared)
#De r_squared is best hoog 82.2% dus de best goed model

#f.
data_test['x2'] = data_test['x'] ** 2
X = sm.add_constant(data_test.iloc[:,1:3])

model = sm.OLS(data_test['y'], X)
results = model.fit()

predicted_test_y = results.predict(X)

r_squared_new = results.rsquared
print(r_squared_new)

#De nieuwe r squared is hoger dus het model werkt goed


