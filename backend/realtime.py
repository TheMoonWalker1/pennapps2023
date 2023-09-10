import ee

# Initialize the Earth Engine API
ee.Initialize()

# Input latitude and longitude from the user
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

# Create a point geometry using the user-provided coordinates
point = ee.Geometry.Point(longitude, latitude)

# Define the ImageCollection to fetch data from
image_collection = ee.ImageCollection("IDAHO_EPSCOR/GRIDMET")

# Filter the ImageCollection by location
filtered_collection = image_collection.filterBounds(point)

# Sort the collection by time in descending order to get the latest data
sorted_collection = filtered_collection.sort("system:time_start", False)

# Get the latest image in the collection
latest_image = sorted_collection.first()

# Select the desired bands and properties
data = latest_image.select(['eto', 'pr', 'rmax', 'rmin', 'tmmn', 'tmmx', 'vpd', 'vs'])

# Get the image properties as a dictionary
properties = latest_image.getInfo()

# Extract the timestamp from the image properties
timestamp = properties['properties']['system:time_start']

# Convert the timestamp to a human-readable format
from datetime import datetime
timestamp = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

# Print the data and timestamp
print("Data at latitude {} and longitude {} on {}: {}".format(latitude, longitude, timestamp, data.getInfo()))
# Extract numeric values from the data dictionary
numeric_values = {band['id']: latest_image.select(band['id']).reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=point,
    scale=30  # Adjust the scale as needed
).get(band['id']).getInfo() for band in dict(data.getInfo())['bands']}

import pickle
def load_xgboost_model(model_file):
    with open(model_file, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

loaded_xgb_model = load_xgboost_model('xgb_model.pkl')

user_input = {
    'm': float(datetime.utcfromtimestamp(properties['properties']['system:time_start'] / 1000).strftime('%m')),
    'day': float(datetime.utcfromtimestamp(properties['properties']['system:time_start'] / 1000).strftime('%d'))
}
# Print the numeric values
for band, value in numeric_values.items():
    print(f"{band}: {value}")
    user_input[band] = float(value)

user_input['lat'] = latitude
user_input['lon'] = longitude

import pandas as pd
user_input_df = pd.DataFrame([user_input])

# Make predictions using the loaded model and user input
predictions = loaded_xgb_model.predict(user_input_df)

# 'predictions' will contain the predicted values
print(f"Predicted value: {predictions[0]}")
