# a = int(input())
# if a % 10 < 5 and a % 10 != 0 and a % 10 != 1:
#     print(a, 'программиста')
# elif a % 10 >= 5:
#     print(a, 'программистов')
# elif a % 10 == 1:
#     print(a, 'программист')
# elif a % 10 == 0:
#     print(a, 'программистов')
#-------------------------------------------------------------------------------
# a = list(str(input()))
# # print(a)
#
# if int(a[0]) + int(a[1]) + int(a[2]) ==  int(a[3]) + int(a[4]) + int(a[5]):
#     print('Счастливый')
# else:
#     print('Обычный')
#-------------------------------------------------------------------------------
# summ_sqrt = 0
# summ = 0
# a = int(input())
# summ += a
# b = [a]
# while summ != 0:
#     a = int(input())
#     summ += a
#     b.append(a)
# # print(b)
# for i in b:
#     summ_sqrt += i ** 2
# print(summ_sqrt)
#-------------------------------------------------------------------------------
# a = int(input())
# b = list(i + 1 for i in range(a))
# bt = list(i for i in range(a))
# temp_b = []
#
#
# for i in b:
#     if i > 9:
#         m = (str(i) + (str(i) * bt[i - 1]))
#         temp_b.append(m)
#         continue
#     m = str(i) + (str(i) * bt[i - 1])
#     temp_b.append(m)
#
# print(temp_b)
