# # import matplotlib.pyplot as plt
# # # import math
# # import numpy as np
# #
# # # def func(x):
# # #     return 0.05 * (x - 1) ** 2 + (3 - 2.9 * np.exp ** (-2.77257 * x ** 2)) * (1 - np.cos(x * (4 - 50 * np.exp ** (-2.77257 * x ** 2))))
# # limit_one = -2
# # limit_two = 2
# #
# # x = np.linspace(limit_one, limit_two, 150)
# # y_one = 0.05 * (x - 1) ** 2 + (3 - 2.9 * np.e ** (-2.77257 * x ** 2)) * (1 - np.cos(x * (4 - 50 * np.e ** (-2.77257 * x ** 2))))
# #
# #
# # fig, ax = plt.subplots()
# # ax.plot(x, y_one)
# # plt.show()
# #--------------------------------------------------------------
# # import plotly.express as px
# # import numpy as np
# #
# # x = np.linspace(0, 10, 150)
# # def f(x):
# #     return x**2
# #
# # px.scatter(x=x, y=f(x)).show()
# #--------------------------------------------------------------
# #
# import matplotlib.pyplot as plt
# # import math
# import numpy as np
#
# # def func(x):
# #     return 0.05 * (x - 1) ** 2 + (3 - 2.9 * np.exp ** (-2.77257 * x ** 2)) * (1 - np.cos(x * (4 - 50 * np.exp ** (-2.77257 * x ** 2))))
# limit_one = 10
# limit_two = 100
#
# x = np.linspace(limit_one, limit_two, 150)
# y_one = (np.sin(np.cos(x ** 2 + np.sin(x ** 3 - 1)))) / (np.cos(x ** 2) ** 2 + np.sin(1 / (x - 1)) ** 2) + ((abs(np.cos(x) ** 2 - np.sin(x) ** 3)) ** 0.5) / (np.cos(np.cos(np.cos(np.cos(x)))))
# fig, ax = plt.subplots()
# ax.plot(x, y_one)
# plt.show()
# #--------------------------------------------------------------
# # a = list(map(int, input().split()))
# # print(max(a))
#
# # a = int(input())
# # b = int(input())
# # c = []
# # c.append(a)
# # c.append(b)
# # print(min(c))
# #
# # a = input()
# # print(a.replace('0', '8'))
# # print(a.count('1'))

# a = []
# for i in range(1, 101):
#     if str(i).find('3') != -1 and i % 2 == 0:
#         a.append(i)
#
# print(sum(a))

# print(bin(42), hex(42), oct(42))

# a = input()
# print(a.replace('0', '8'))
# print(a.count('1'))

# s = []
# for i in range(1, 100 + 1):
#     if str(i).find('3') != -1 and i % 2 != 0:
#         s.append(i)
# print(sum(s), s)
# i = 0
# while True:
#     print(hex(i))
#     i += 1
#     if i == 100:
#         break
# import matplotlib.pyplot as plt
# import numpy as np
#
# # def func(x):
# #     return 0.05 * (x - 1) ** 2 + (3 - 2.9 * np.exp ** (-2.77257 * x ** 2)) * (1 - np.cos(x * (4 - 50 * np.exp ** (-2.77257 * x ** 2))))
# limit_one = -2
# limit_two = 2
#
# # x = np.linspace(limit_one, limit_two, 150)
# x = np.arange(limit_one, limit_two, 0.001)
# y_one = np.sin(1 / x)
#
#
# fig, ax = plt.subplots()
# ax.plot(x, y_one)
# plt.show()

#----------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import cm
#
# fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
#
# x = np.arange(-2, 2, 0.01)
# y = np.arange(-2, 2, 0.01)
# z = np.arange(-2, 2, 0.01)
# # x, y = np.meshgrid(x, y)
#
# def f(x, y, z):
#     return 10 * 3 + ((x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y)) + (z ** 2 - 10 * np.cos(2 * np.pi * z)))
#
# s = f(x, y, z)
# print(s)
# surf = ax.plot_surface(x, y, z, cmap = cm.viridis, linewidth=0, antialiased=False)
#
# plt.show()

#----------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import cm
#
# fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
#
# x = np.arange(-50, 50, 0.1)
# y = np.arange(-50, 50, 0.1)
#
# x, y = np.meshgrid(x, y)
# A = [-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0,  16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32]
# B = [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]
# # z = 10 * 2 + ((x ** 2) - 10 * np.cos(2 * np.pi * x)) + (y ** (2) - 10 * np.cos(2 * np.pi * y))
# summ = 0
# n = 1
# for i, l in zip(A, B):
#     summ += (n + (x - i) ** 6 + (y - l) ** 6) ** -1
#     n += 1
# z = 1 /  ((1 / 500) + summ)
#
# # print(z)
#
#
# surf = ax.plot_surface(x, y, z, cmap = cm.viridis, linewidth=0, antialiased=False)
#
# plt.show()

#----------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
#
# fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
# x = [-200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
# y = [-3.36, -2.20, 0, 2.81, 5.96, 9.32, 12.75, 16.21, 19.62, 22.96, 26.23, 29.41, 32.52, 35.56, 38.51, 41.35, 44.04]
# z = [2.39, 1.29, 0, -1.29, -2.17, -2.89, -3.64, -4.43, -5.28, -6.18, -7.08, -7.95,  -8.79, -9.58, -10.34, -11.06, -11.77]
# print(len(x))
# print(len(y))
# print(len(z))
# plot = ax.scatter(x, y, z)
#
#
#
# plt.show()



x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 6, 0.2)
x, y = np.meshgrid(x, y)


def f(x, y):
    s = 0
    for i in range(10):
        s+= (np.e ** (-i * x / 10) - 5 * np.e ** (-i * y / 10) - np.e ** (-i / 10) + 5 * np.e ** (-i)) ** 2
    return s
# z = np.zeros(x.shape)
# for j in range(x.shape[1]):
#     for i in range(y.shape[0]):
#         xx, yy = x[0][j], y[i][0]
#         z[i][j] = xx**2+yy**2
z = f(x, y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(x, y, z, cmap=cm.plasma,
                       linewidth=0, antialiased=False)
plt.show()
