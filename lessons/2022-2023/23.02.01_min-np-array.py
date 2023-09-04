import numpy as np
import math
x = np.array([4, 3, 2, 2])
x = list(set(x))
m = math.inf
for i in range(len(x) - 1):
    if i == len(x) - 1 and x[i] > x[i + 1]:
        m = x[i - 1]
        break
    if x[i] < m:
        m = x[i]



print(m)