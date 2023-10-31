import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import sklearn as sk
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
import seaborn as sns

# Exercise 1: Fitting a model
print('Exercise 1')
np.random.seed(2)

x = np.random.uniform(0, 10, 200)
y = 2 * x**2 - 5 * x + 3 + np.random.normal(0, 10, 200)
def exercise1(x,y):
    """Function with all the subquestions of exercise 1"""
    #a
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
    print('c. Second polynomial') 

    #d
    df_train['x2'] = df_train['x']**2
    X = sm.add_constant(df_train.iloc[:,1:3])
    model = sm.OLS(df_train['y'], X)
    results = model.fit()

    predict_train_y = results.predict(X)
    print('d.')
    plt.scatter(df_train['x'], df_train['y'])
    plt.scatter(df_train['x'], predict_train_y, color = 'red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Regression Model (Degree 2)')
    plt.show()

    #e
    R2 = results.rsquared
    mse = mean_squared_error(df_train['y'], predict_train_y)
    print(f'e. R2: {R2}, mse: {mse}')

    df_test['x2'] = df_test['x']**2
    X = sm.add_constant(df_test.iloc[:,1:3])
    model = sm.OLS(df_test['y'], X)
    results = model.fit()
    predict_test_y = results.predict(X)
    R2 = results.rsquared
    mse = mean_squared_error(df_test['y'], predict_test_y)
    #f
    print('f. The R2 of the test sample is lower than the training sample. The MSE of the test sample is way lower than the training sample which is also positive. This means that the model is good in predicing.')
print(exercise1(x, y))

#Data outlier functions exercise 2:
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
print('Exercise 2')
#a 
df = pd.read_excel('winequality-red.xlsx')
def exercise2 (df):
    #b
    print('b. check')

    #c
    df = outlier_drops(df)
    print('c. there are no missing values')
    
    #d 
    print('d.')
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
    print('g.')
    print(f'R2 trainig: {R2}')

    X = sm.add_constant(df_test_x)
    model = sm.OLS(df_test_y, X)
    results = model.fit()
    predict_test_y = results.predict(X)
    R2 = results.rsquared
    print(f'R2 test: {R2}')
    
    #i
print(exercise2(df))

#Exercise 3.1 Post-processing of predictions:                   Doet er wat langer over
print('Exercise 3.1')
df_actual = pd.read_excel('training.xlsx')
df_prediction = pd.read_excel('predictions_training.xlsx')

df_actual['UOI'] = np.zeros(len(df_actual))
def UOI_cells(df_actual, df_prediction):
    """Returns the mean UOI"""
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
#Y = np.array(df_actual.iloc[:,6]).reshape(-1, 1)           Werkt niet 
#model = LogisticRegression()
#model.fit(X, Y)