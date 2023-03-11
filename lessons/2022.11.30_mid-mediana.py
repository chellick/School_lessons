# s = [1, 2, 3, 4, 5]
# print(max(el), min(el), sum(el) / len(el))
# # медиана - среднее значение
#
# x_temp = sorted(s)
#
# if len(x_temp) % 2 == 1:
#     med = x_temp[len(x_temp)//2]
# else:
#     med = (x_temp[len(x_temp) // 2 - 1] + x_temp[len(x_temp) // 2]) / 2
# print(med)
#----------------------------------------------------------------------------------
# s = [5, 4, 7, -10, 11]
# def mediana(el):
#     for strok in range(len(el) - 1):
#         for g in range(len(el) - 1 - strok):
#             if el[g] > el[g + 1]:
#                 el[g], el[g + 1] = el[g + 1], el[g]
#     print(el)
#     if len(el) % 2 == 1:
#         med = el[len(el) // 2]
#     else:
#         med = (el[len(el) // 2 - 1] + el[len(el) // 2]) / 2
#     return med
#
# print(mediana(s))
#----------------------------------------------------------------------------------
# s = [5, 4, 7, -10, 11]
# d = []
#
#
# d.append(s.pop(0))
# print(d, s)
# # b = []
# # for strok in s

# sort
# def sort_bubble(el):
#     for strok in range(len(el) - 1):
#         for g in range(len(el) - 1 - strok):
#             if el[g] > el[g + 1]:
#                 el[g], el[g + 1] = el[g + 1], el[g]
#     return el
#
# s = [5, 4, 7, -10, 11]
# print(sort_bubble(s))


