import ee

# Authenticate to Earth Engine using your credentials (if required)
# ee.Authenticate()

# Initialize the Earth Engine API
ee.Initialize()

# Define the ImageCollection
collection = ee.ImageCollection("IDAHO_EPSCOR/GRIDMET")

# Input latitude and longitude from the user
latitude = float(input("Enter Latitude: "))
longitude = float(input("Enter Longitude: "))

# Create a point geometry for the user-specified location
point = ee.Geometry.Point(longitude, latitude)

# Filter the collection based on time and location
filtered_collection = collection.filterBounds(point).sort('system:time_start', False)

# Get the latest image from the filtered collection
latest_image = filtered_collection.first()

# Print the latest image information
print("Latest Image ID:", latest_image.id())
print("Date of Latest Image:", ee.Date(latest_image.get('system:time_start')).format('YYYY-MM-dd').getInfo())

# Optionally, you can visualize the image using the Map
# Uncomment the following lines if you have the ipygee library installed
# import ipygee as ui
# Map = ui.Map()
# Map.centerObject(point, 6)
# Map.addLayer(latest_image, {}, "Latest Image")
# Map

# You can also export the image if needed
# Export.image.toDrive({
#     image: latest_image,
#     description: 'latest_image',
#     folder: 'GEE_outputs',
#     scale: 1000,  # Set the scale according to your requirements
# })
