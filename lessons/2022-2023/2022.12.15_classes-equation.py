# import matplotlib.pyplot as plt
#
# class Equation:
#     def __init__(self, el, a, b, c):
#         self.y = None
#         self.el = el
#         self.a = a
#         self.b = b
#         self.c = c
#         # self.y = self.a  * self.el ** 2 + self.b * self.el + self.c
#
#     def count(self):
#         self.y = self.a  * self.el ** 2 + self.b * self.el + self.c
#         return self.y
#
# task = Equation(10, 10, 10, 10)
# task.count()
#
# figure, axis = plt.subplots()
# axis.scatter(task.el, task.y)
# plt.show()
#------------------------------------------------------------------------------
#
# times = int(input())
# game = dict()
#
# list_games = [input().split(';') for i in range(times)]
# for i in range(times):
#     for h in list_games:
#         for my_tuple in range(len(h)):
#             if h[my_tuple] is int:
#
# print(list_games, game)
#------------------------------------------------------------------------------
# times = int(input())
# list_games = [input().split(';') for i in range(times)]
# # print(list_games)
# draw = 0
# win = 0
# loose = 0
# first_results = [0, 0, 0, 0, 0]
# second_results = []
#
# for i in list_games:
#     temp_game = i
#     for val in temp_game:
#         first_team = temp_game[0]
#         second_team = temp_game[2]
#         if val[1] > val[3]:
#             first_results
#         elif val[1] == val[3]:
#             draw += 1
#         elif val[1] < val[3]:
#             win += 1
#             second_results.append(win)
#         first_results

#------------------------------------------------------------------------------
# times = int(input())
# right_list = []
# strings_list = []
# for i in range(times):
#     right_list.append(str(input()))
# # print(right_list)
# strings = int(input())
# for i in range(strings):
#     strings_list.append(str(input()))
#------------------------------------------------------------------------------
# import math
# range_one = []
# for i in range(-14, 13):
#     range_one.append(i)
#     i += 1
#
#
# range_two = []
# for i in range(15, 17):
#     range_two.append(i)
#     i += 1
#
# num = int(input())
# if num in range_one or num in range_two or num > 19:
#     print(True)
# else:
#     print(False)
#------------------------------------------------------------------------------
#
# a = float(input())
# b = float(input())
# com = str(input())
# if com == 'div':
#     if b == 0.0:
#         print('Деление на 0!')
#     else:
#         print(a // b)
#
# elif com == 'mod':
#     if b == 0.0:
#         print('Деление на 0!')
#     else:
#         print(a % b)
# elif com == 'pow':
#     print(a ** b)
# elif com == '+':
#     print(a + b)
# elif com == '-':
#     print(a - b)
# elif com == '*':
#     print(a * b)
# elif com == '/':
#     if b == 0.0:
#         print('Деление на 0!')
#     else:
#         print(a / b)
#
#------------------------------------------------------------------------------
# fig = str(input())
# Pi = 3.14
# if fig == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     print((p * (p - a) * (p - b) * (p - c) )** 0.5)
# elif fig == 'круг':
#     r = int(input())
#     print(Pi * r ** 2)
# elif fig == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     print(a * b)
#------------------------------------------------------------------------------
# listnum = []
#
# a = int(input())
# b = int(input())
# c = int(input())
# listnum.append(a)
# listnum.append(b)
# listnum.append(c)
# listnum = sorted(listnum)
# print(listnum.pop())
# print(listnum.pop(0))
# print(listnum.pop(0))
# # print(list)
#------------------------------------------------------------------------------
# a = int(input())
# if a % 10 < 5 and a % 10 != 0 and a % 10 != 1:
#     print(a, 'программиста')
# elif a % 10 >= 5 and a :
#     print(a, 'программистов')
# elif a % 10 == 1:
#     print(a, 'программист')
# elif a % 10 == 0:
#     print(a, 'программистов')
