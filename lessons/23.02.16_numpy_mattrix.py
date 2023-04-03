import numpy as np

p = [[1, 3],
     [2, 4]]

t = [[5, 6],
     [7, 8]]

c = np.hstack((p, t))

print(c.T)

