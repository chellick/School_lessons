import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, coords):
        self.coords = coords
        self.g = 0
        self.h = 0
        
        
def vector_length(point1, point2):
    x1, y1 = point1.coords
    x2, y2 = point2.coords
    return ((x2-x1) ** 2 + (y2-y1) ** 2)

def f(g, h):
    return g + h


def A(start, goal, points: list):
    current_state = start
    current_f = f(vector_length(start, current_state), vector_length(current_state, goal))
    opened_points = points
    closed_points = [start]
    
    while len(opened_points) != 0:
        for point in opened_points:
            if f(vector_length(start, point), vector_length(point, goal)) <= current_f:
                current_f = f(vector_length(start, point), vector_length(point, goal))
                current_state = point
                print(current_state)
        
        closed_points.append(current_state)
        opened_points.pop(opened_points.index(current_state))
        print(len(opened_points))
        
        
    return current_state

def plot_points(start, goal, points):
    x = []
    y = []
    for i in points:
        x.append(i.coords[0])
        y.append(i.coords[1])
    
    plt.scatter([start.coords[0], goal.coords[0]], [start.coords[1], goal.coords[1]])
    plt.scatter(x, y)
    plt.show()
    
                
            