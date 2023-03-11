# class PLayer:
#     def __init__(self,  sex, height, weight):
#         self.__sex = sex
#         self.__height = height
#         self.__weight = weight
#
#     def get_atributes(self):
#         print(self.__sex)
#         print(self.__weight)
#         print(self.__height)
#
# Petar = PLayer('male', 120, 70)
#-----------------------------------------------------------------------
# a, b = map(int, input().split())
# mat = []
# for i in range(a):
#     mat1 = list(map(int, input().split()))
#     mat.append(mat1)
# maximum = mat[0][0]
# index = 0, 0
# for i in range(a):
#     for j in range(b):
#         if maximum < mat[i][j]:
#             maximum = mat[i][j]
#             index = i, j
# print(*index, sep=" ")

#------------------------------------------------------------------------
# import numpy as np
# a, b = map(int, input().split())
# mat = []
# for i in range(a):
#     mat1 = list(map(int, input().split()))
#     mat.append(mat1)
#
# array = np.array(mat)
# print(*np.unravel_index(np.argmax(array), array.shape), sep = ' ')

#------------------------------------------------------------------------------
# a = int(input())
# mat = []
# for i in range(a):
#        row = []
#        for j in range(a):
#               row.append('.')
#        mat.append(row)



#------------------------------------------------------------------------------
#
# a = int(input())
# mat = []
# for i in range(a):
#     row = []
#     for j in range(a):
#         row.append(0)
#     mat.append(row)
# # print(mat)
# for i in range(a):
#     mat[i][-i - 1] = 1
#     for j in range(a - i, a):
#         mat[i][j] = 2
# for i in range(a):
#     print(*mat[i], sep = ' ')
#-------------------------------------------------------------------------------
# a, b = map(int, input().split())
# mat = []
#
# for j in range(b * a):
#     mat.append(j + 1)
#     mat.append(0)
# temp_mat = []
# mat = mat[:a * b]
# mass = []
# for i in range(a):
#     temp_mat.append(mat[:b])
#     del mat[:b]
#     mass = []
#
#
# if len(temp_mat) > 4:
#     for i in range(a):
#         if i % 2 != 0:
#             temp_mat[i].insert(0, 0)
#             del temp_mat[i][-1]
#
#
# for i in range(a):
#     print(*temp_mat[i], sep=' ')
# print(mass)
# print(mat, sep = ' ')
#-------------------------------------------------------------------------------
# mat = []
# n, m= map(int, input().split())
# el = 1
# count = 0
# for i in range(n):
#     row = []
#     for j in range(m):
#         if (i + j) % 2 == 0:
#             count += 1
#             el = count
#         else:
#             el = 0
#         row.append(el)
#     mat.append(row)
# for i in range(n):
#     print(*mat[i], sep=" ")
#------------------------------------------------------------------------------
# a, b = map(int, input().split())
# num = int(input())
# mat = []
# row = []
#
#
# for i in range(a):
#     row = []
#     for j in range(b):
#         row.append(j)
#     mat.append(row)
#
# for i in range(a):
#     print(*mat[i], sep = ' ')
# for i in range(num):
    