import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Position vector
r = np.array([2, 1, 0])

# Force vectors
F1 = np.array([0, 10, 0])
F2 = np.array([0, 0, -5])

# Calculate torques
tau1 = np.cross(r, F1)
tau2 = np.cross(r, F2)
tau_net = tau1 + tau2

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, *r, color='blue', label='Position Vector r')
ax.quiver(*r, *F1, color='green', label='Force F1')
ax.quiver(*r, *F2, color='orange', label='Force F2')
ax.quiver(0, 0, 0, *tau_net.flatten(), color='red', label='Net Torque')  # flatten in case needed

# Axes settings
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Torque on Robotic Arm')
ax.legend()
plt.show()

