# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the system
radar_sensitivity = -150 # dBsm
telescope_resolution = 0.1 # arcseconds

# Define the range of debris object sizes
debris_object_sizes = np.logspace(-3, 0, 100) # meters

# Calculate the system's sensitivity and resolution for each debris object size
system_sensitivity = radar_sensitivity + 10 * np.log10(debris_object_sizes)
system_resolution = telescope_resolution / debris_object_sizes

# Plot the system's sensitivity and resolution curves
plt.plot(debris_object_sizes, system_sensitivity, label='Sensitivity (dBsm)')
plt.plot(debris_object_sizes, system_resolution, label='Resolution (arcseconds)')

# Set the plot labels and limits
plt.xlabel('Debris object size (m)')
plt.ylabel('System performance')
plt.legend()
plt.xlim([1e-3, 1e0])
plt.ylim([-180, 2])

# Save the plot to a file
plt.savefig('system_performance.png')
