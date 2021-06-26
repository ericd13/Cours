Ex = [0, -2, 1, -2, -2, -1, 2, 3, 3, 0, 0, 0, 1, 2, 0,
      -2, -1, -1, 1, 3, 3, 1, 3, 0, 2, -1, -1, 1, 1, 1]

Expr = "1+2*(7-(4-3)*((2-5)+2*((12/4-8)+2*3)))"


import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import ascent


a = np. array([[1, 0.5, 1, 0, 1],
               [0, 0, 1, 1, 0.2],
               [0.8, 0, 1, 0, 1]])

b = ascent()

c = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        x = (i-50)/20
        y = (j-50)/20
        c[i,j] = np.sin(x*x+y*y)

image4 = ascent()
plt.gray()
plt.imshow(c)
plt.show()


