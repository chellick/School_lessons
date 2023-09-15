from typing import Any
import numpy as np
import matplotlib.pyplot as plt
from backendA import *


points = np.array([Point([np.random.randint(0, 100) for _ in range(2)]) for _ in range(10)])

start = Point([np.random.randint(0, 100) for _ in range(2)])
goal = Point([np.random.randint(0, 100) for _ in range(2)])


    