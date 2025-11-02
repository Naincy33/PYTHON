import numpy as np
import matplotlib.pyplot as plt

# Original vector
v = np.array([2, 1])

# Transformation matrix (Rotate 90°)
theta = np.radians(120)
A = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# Apply transformation
v_transformed = A @ v

# Plotting
plt.figure(figsize=(6,6))
plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)

# Original vector
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original')

# Transformed vector
plt.quiver(0, 0, v_transformed[0], v_transformed[1], angles='xy', scale_units='xy', scale=1, color='red', label='Transformed')

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title("Linear Transformation: Rotation by 90°")
plt.show()
