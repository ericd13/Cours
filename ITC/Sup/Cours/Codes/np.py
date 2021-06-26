import numpy as np
import matplotlib.pyplot as plt


# graphe de x -> sin(x**2) sur [-1 ; 5]

# X = np.linspace(-1, 5, 1000)
# Y = np.sin(X**2)
# 
# plt.plot(X, Y)
# plt.show()

T = np.linspace(-5, 5, 1000)
X = np.sin(5*T)
Y = np.cos(3*T)
plt.plot(X, Y)
plt.show()