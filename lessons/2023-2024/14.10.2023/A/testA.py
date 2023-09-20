from backendA import *
import numpy as np


start = Point([0, 0])
goal = Point([10, 10])

points = [Point([1, 1]), Point([2, 3]), Point([4, 5]), Point([7, 8]), Point([10, 0])]
plot_points(start, goal, points)

print(f(vector_length(start, Point([1, 1])), vector_length(Point([1, 1]), goal)))
print(f(vector_length(start, Point([2, 3])), vector_length(Point([2, 3]), goal)))

# print(A(start, goal, points))
