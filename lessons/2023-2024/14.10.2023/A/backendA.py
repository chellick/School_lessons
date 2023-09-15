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


def A(start, goal, points):
    current_f = f(vector_length(start, start), vector_length(start, goal))
    current_state = start
    opened_points = []
    closed_points = [start]
    
    for point in points:
        if f(vector_length(start, point), vector_length(point, goal)) < current_f:
            current_f = f(vector_length(start, point), vector_length(point, goal))
            current_state = point
            
        
    


    
    
