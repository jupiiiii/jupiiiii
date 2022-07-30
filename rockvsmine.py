# -*- coding: utf-8 -*-
"""RockVsMine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gI-gD3Y0iWSRPeYXNraf0rjm43wVJq_X

Importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and data processing"""

sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header = None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""Split data set"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

"""Training the logistic regression model with training data"""

print(X_train, Y_train)

model = LogisticRegression()

model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy on training data
"""

X_train_predicition = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_predicition, Y_train)

print(training_data_accuracy)

"""Accuracy on test data"""

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print(test_data_accuracy)

"""making prediction system"""

input_data1 = (0.0346,0.0509,0.0079,0.0243,0.0432,0.0735,0.0938,0.1134,0.1228,0.1508,0.1809,0.2390,0.2947,0.2866,0.4010,0.5325,0.5486,0.5823,0.6041,0.6749,0.7084,0.7890,0.9284,0.9781,0.9738,1.0000,0.9702,0.9956,0.8235,0.6020,0.5342,0.4867,0.3526,0.1566,0.0946,0.1613,0.2824,0.3390,0.3019,0.2945,0.2978,0.2676,0.2055,0.2069,0.1625,0.1216,0.1013,0.0744,0.0386,0.0050,0.0146,0.0040,0.0122,0.0107,0.0112,0.0102,0.0052,0.0024,0.0079,0.0031)
#change the input data into numpy array
input_data_numpy_array1 = np.asarray(input_data1)

#reshape the np array because we are predicting for only one instance
input_data_reshaped1 = input_data_numpy_array1.reshape(1,-1)

prediction1 = model.predict(input_data_reshaped1)
if prediction1[0] == 'R':
  print("The object is rock")
else:
  print("The object is mine")

input_data2 = (0.0188,0.0370,0.0953,0.0824,0.0249,0.0488,0.1424,0.1972,0.1873,0.1806,0.2139,0.1523,0.1975,0.4844,0.7298,0.7807,0.7906,0.6122,0.4200,0.2807,0.5148,0.7569,0.8596,1.0000,0.8457,0.6797,0.6971,0.5843,0.4772,0.5201,0.4241,0.1592,0.1668,0.0588,0.3967,0.7147,0.7319,0.3509,0.0589,0.2690,0.4200,0.3874,0.2440,0.2000,0.2307,0.1886,0.1960,0.1701,0.1366,0.0398,0.0143,0.0093,0.0033,0.0113,0.0030,0.0057,0.0090,0.0057,0.0068,0.0024)
#change the input data into numpy array
input_data_numpy_array2 = np.asarray(input_data2)

#reshape the np array because we are predicting for only one instance
input_data_reshaped2 = input_data_numpy_array2.reshape(1,-1)

prediction2 = model.predict(input_data_reshaped2)
if prediction2[0] == 'R':
  print("The object is rock")
else:
  print("The object is mine")