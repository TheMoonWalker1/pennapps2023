import netCDF4 as nc

# Open the NetCDF file for reading
file_path = 'gridmet/tmmn_2023.nc'
dataset = nc.Dataset(file_path, 'r')

# Print information about the dataset
print("NetCDF File Information:")
print(f"File: {file_path}")
print(f"Format: {dataset.file_format}")
print(f"Dimensions: {dataset.dimensions}")
print(f"Variables: {dataset.variables}")
print("\n")

# Access and print variable data
for var_name, var in dataset.variables.items():
    print(f"Variable: {var_name}")
    print(f"Dimensions: {var.dimensions}")
    print(f"Shape: {var.shape}")
    print(f"Data: \n{var[:]}")  # Access the data using slicing
    print("\n")

# Close the NetCDF file
dataset.close()
