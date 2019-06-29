import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor
pd.set_option('display.max_rows', 50000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)
mel_data_filepath = os.getcwd()+ "/Resources/CSV/melb_data.csv"
#print(mel_data_filepath)
data = pd.read_csv(mel_data_filepath)
print(data)
#print(data.dropna(axis=0))
#print(data.describe())
y = data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[melbourne_features]
#print(X.describe())
#print(data)
#print(X.head())
melbourne_model = DecisionTreeRegressor(random_state=1)
# Fit model
melbourne_model.fit(X, y)
'''
DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=2,
           max_leaf_nodes=None, min_impurity_decrease=0.0,
           min_impurity_split=None, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           presort=False, random_state=1, splitter='best')
'''
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))