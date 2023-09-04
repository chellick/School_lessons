
# def sort_change(el):
#     for strok in range(len(el)):
#         for g in range(len(el)):
#             if el[strok] > el[g]:
#                 el[strok], el[g] = el[g], el[strok]
#     return el
#
# s = [5, 4, 7, -10, 11]
# print(sort_change(s))

#----------------------------------------------------------------------------------------------

# s = [11, 10, 3, 14]
# def summ(n):
#     cor = sum(map(int, list(str(n))))
#     return cor
#
# def sort_change(el):
#     for strok in range(len(el)):
#         for g in range(len(el)):
#             if summ(el[(strok)]) < summ(el[g]):
#                 el[strok], el[g] = el[g], el[strok]
#     return el
#
#
# print(sort_change(s))
#----------------------------------------------------------------------------------------------
# s = [11, 3, 14, 10]
# b = [112, 32, 142, 102]
# def sort_bubble(el, y):
#     for strok in range(len(el) - 1):
#         for g in range(len(el) - 1 - strok):
#             if el[g] > el[g + 1]:
#                 el[g], el[g + 1] = el[g + 1], el[g]
#                 y[g], y[g + 1] = y[g + 1], y[g]
#     return y
# print(sort_bubble(s, b))

# #----------------------------------------------------------------------------------------------
#
# name = (input().split())
# s = (input().split())
#
# def sort_bubble(el, y):
#     x1 = ''
#     y1 = ''
#     for strok in range(len(el)):
#         for g in range(len(el)):
#             if el[strok] > el[g]:
#                 el[strok], el[g] = el[g], el[strok]
#                 y[strok], y[g] = y[g], y[strok]
#     x1 = "".join(el)
#     y1 = "".join(y)
#     return x1, y1
# m = sort_bubble(s, name)
#----------------------------------------------------------------------------------------------

# print(chr(129440))
#----------------------------------------------------------------------------------------------
# Написать программу, которая запрашивает строковые переменные love, life с количеством символов не более 10 и выполняет следующие:
#
# Находит количество символов в переменных
# Возводит большее число в меньшую степень
# Складывает переменные так, чтобы между ними был пробел
# Выводит эту пару ровно столько раз, сколько получилось в п. 2, между парами тоже стоит пробел
# Порядок вывода по сравнению с вводом, не менять

# def count_str(el):
#     length = 0
#     for strok in el:
#         length += 1
#     return length
#
# love = str(input())
# life = str(input())
# if count_str(love) > count_str(life):
#     c = count_str(love) ** count_str(life)
# for strok in range(c):
#     print(love, life, sep = " ",  end = ' ')
#----------------------------------------------------------------------------------------------


# print(count_str(love), life)