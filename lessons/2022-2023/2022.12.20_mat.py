# mat = [[1, 2, 3],
#        [1, 2, 3]]
# print(mat)
#---------------------------------- Matrix ------------------------------------
# mat = []
# n, m = 2, 3
# for i in range(n):
#        row = []
#        for j in range(m):
#               row.append(1)
#        mat.append(row)
# # print(*mat, sep='\n')
# s = 0
# for i in range(n):
#        for j in range(m):
#               s += mat[i][j]
#
# print(s)
# for i in range(n):
#      print(*mat[i], sep = ' ')

#--------------------------------------------
# a, b = map(int, input().split())
# mat = []
# for i in range(a):
#     row = []
#     for j in range(b):
#         row.append(0)
#     mat.append(row)
# # for i in range(b):
# #     print(*mat[i], sep = ' ')
#
# #--------------------------------------------
# a, b = map(int, input().split())
# mat = []
# for i in range(a):
#     row = []
#     for j in range(b):
#         row.append(j + 1)
#     mat.append(row)
# for i in range(a):
#     print(*mat[i], sep=' ')
#
# s = 0
# for i in range(a):
#        for j in range(a):
#               s += mat[i][j]
# print(s)
#---------------------------------------
# a = int(input())
# mat = []
# for i in range(a):
#     mat1 = list(map(int, input().split()))
#     mat.append(mat1)
#
# for i in range(a):
#     print(*mat[i], sep =' ')
#---------------------------------------
# a = int(input())
# mat = []
# for i in range(a):
#     mat1 = list(map(int, input().split()))
#     mat.append(mat1)
#
# for i in range(a):
#     print(*mat[i], sep =' ')
#
# summa = []
# for i in mat:
#     summa.append(sum(i))
#
# for j in range(mat):
#     for i in range(len(mat[0])):
#         summ = 0
#         for i in range(a):
#             summ += amt[i][j]
#         print(summ, end=' ')
#
# summ = 0
# for i in range(a):
#     for j in range(len(mat[0])):
#         if i == j:
#             summ += mat[i][j]
#         print(summ, end =' ')

#-----------------------------------------------
# a = int(input())
# mat = []
# summ = 0
# for i in range(a):
#     mat1 = list(map(int, input().split()))
#     mat.append(mat1)
#
#
# for r in range(a):
#     summ += mat[r][-r - 1]
# print(summ, end =' ')









# Допустим (a) является матрицей, соответственно она имее два элемента (для двоичной матрицы)
a = [[1, 2, 3], [1, 2, 3], [1, 2 ,3]]
# Матрица: Массив в массиве
# Массив — это поименованная совокупность однотипных элементов, упорядоченных по индексам, определяющим положение элемента в массиве.
# Можно утверждать, что матрица - набор элементов имеющих два индекса
# Если мы хотим получить элемент '2', то нам нужно обрптиться к: elem = a[0][1] НЕ ЗАБЫВАЙ О ТОМ, ЧТО ИНДЕКСАЦИЯ ЭЛЕМЕНТОВ ПРОИСХОДИТ С 0

a = int(input())
mat = []
summ = 0
for i in range(a):
    mat1 = list(map(int, input().split()))
    mat.append(mat1)


for r in range(a):
    summ += mat[r][-r - 1]
print(summ, end =' ')



































