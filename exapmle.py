import pickle

import pandas as pd 

from sklearn.linear_model import LinearRegression   

with open("house_predictor.pickle", "rb") as file:
    loaded_model = pickle.load(file) 

print(loaded_model.coef_ )
print(loaded_model.intercept_ )