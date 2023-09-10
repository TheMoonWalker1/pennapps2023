import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from keras.layers import Dense
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the data
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Step 2: Preprocess the data
# Assuming you want to predict 'swe_snotel'
# Remove unnecessary columns
data = data[['m', 'day', 'eto', 'pr', 'rmax', 'rmin', 'tmmn', 'tmmx', 'vpd', 'vs', 'lat', 'lon', 'elevation', 'aspect', 'curvature', 'slope', 'eastness', 'northness', 'swe_snotel']]

# Fill missing values if necessary
data = data.fillna(0)  # You can change this depending on your data and preprocessing needs

# Split the data into features l7(X) and target (y)
X = data.drop(columns=['swe_snotel'])
y = data['swe_snotel']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=41)

# Create and train an XGBoost regressor
xgb_model = xgb.XGBRegressor(objective="reg:squarederror", random_state=41)
xgb_model.fit(X_train, y_train)

# Make predictions
predictions = xgb_model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error (MSE): {mse:.4f}")

# Calculate R-squared (R2) score
r2 = r2_score(y_test, predictions)
print(f"R-squared (R2) Score: {r2:.4f}")

# # Get the XGBoost booster
# booster = xgb_model.get_booster()
#
# # # Get the tree structure as a list of strings
# tree_structure = booster.get_dump()
# #
# # # Print the tree structure
# for i, tree in enumerate(tree_structure):
#     print(f"Tree {i}:\n{tree}\n")
import pickle

# Export the XGBoost model to a file
with open('xgb_model.pkl', 'wb') as model_file:
    pickle.dump(xgb_model, model_file)
