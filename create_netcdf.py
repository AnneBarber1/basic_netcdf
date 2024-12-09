
'''
This script creates a simple netCDF file with a single variable, U, 
and three dimensions (time, z, y and x)
'''

# Load in libraries
import netCDF4
import numpy as np

# Create a new netCDF file
new_nc_file = 'test_file.nc'
nc_out = netCDF4.Dataset(new_nc_file,'w')

# Define dimensions: x/y/z = 10, time = 5
time_dim = nc_out.createDimension('Time',5)
z_dim = nc_out.createDimension('z_direction',10)
y_dim = nc_out.createDimension('y_direction',10)
x_dim = nc_out.createDimension('x_direction',10)

# Create variable 'u' for horizontal wind speed
u = nc_out.createVariable('U', np.float32, ('Time', 'z_direction', 'y_direction', 'x_direction'))

# Give the variable some attributes and units
u.units = 'm/s'
u.description = 'U component of wind'
u.long_name = 'U component of wind'

# Give the variable values: want the field to have uniform spatial 
# values with a value equal to the current time frame
for i in range(5):
    u[i,:,:,:]=i

# Close the netCDF file
nc_out.close()