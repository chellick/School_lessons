import matplotlib.pyplot as plt
import math
from math import *
import cmath
class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # self.y = self.a  * self.el ** 2 + self.b * self.el + self.c
        self.fl = True
    def discr(self):
        self.discr = self.b ** 2 - 4 * (self.a * self.c)
        if self.a == 0 and self.b == 0:
            if self.c == 0:
                self.fl = False
                self.x1 = -inf
                self.x2 = +inf
                print(f'({self.x1}, {self.x2})')
                return self.x1, self.x2
            else:
                self.fl = False
                print('NO X')
                return
        if self.a == 0:
            self.x1 = -self.c / self.b
            self.y1 = 0
            self.x2 = -self.c / self.b
            self.y2 = 0
            return self.y1, self.x1, self.y2, self.x2


        if self.discr >= 0:
            self.x1 = (-self.b + self.discr ** 0.5) / (2 * self.a)
            self.x2 = (-self.b - self.discr ** 0.5) / (2 * self.a)
            self.y1 = 0
            self.y2 = 0

        if self.discr < 0:
            self.x1 = (-self.b + cmath.sqrt(self.discr)) / (2 * self.a)
            self.x2 = (-self.b - cmath.sqrt(self.discr)) / (2 * self.a)
            self.y1 = 0
            self.y2 = 0

        if self.a == 0:
            self.x1 = -self.c / self.b
            self.y1 = 0
            self.x2 = -self.c / self.b
            self.y2 = 0
            return self.y1, self.x1, self.y2, self.x2
        # else:
        #     print('discr < 0')


a = int(input('введите a: '))
b = int(input('введите b: '))
c = int(input('введите c: '))
task = Equation(a, b, c)
task.discr()
if task.discr >= 0 and task.fl == True:
    figure, axis = plt.subplots()
    axis.scatter(task.x1, task.y1)
    axis.scatter(task.x2, task.y2)
    print('zero func ', task.x1, task.x2)
    print('func', task.y1, task.y2)
    plt.show()
else:
    print('no plot, bro!')
# import cmath
# a = cmath.sqrt(9)
# print(a)
