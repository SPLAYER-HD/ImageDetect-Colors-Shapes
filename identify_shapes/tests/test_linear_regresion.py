"""Test Abyss Solutions"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.linear_model import LinearRegression

list = {'X': [0,11,9,9,18,11],
        'Y': [25,36,45,54,72,83]
       }
data =[[0, 25],[1, 36],[2, 45],[3, 54],[4, 72],[5,83]]
X = np.array(data)[:,0].reshape(-1,1)
y = np.array(data)[:,1].reshape(-1,1)
print("X=")
print(X)
print("y=")
print(y)
to_predict_x= [6]
to_predict_x= np.array(to_predict_x).reshape(-1,1)
regsr=LinearRegression()
regsr.fit(X,y)
predicted_y= regsr.predict(to_predict_x)
m= regsr.coef_
c= regsr.intercept_
print("Predicted y:\n",predicted_y)
print("slope (m): ",m)
print("y-intercept (c): ",c)