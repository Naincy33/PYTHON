import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1], [2], [3]])
b = np.array([[10, 20, 30]])

result = a + b

plt.imshow(result, cmap='viridis', interpolation='nearest')
plt.title("Broadcasted Result")
plt.colorbar()
plt.show()
