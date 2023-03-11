#
# s = [19, 0, 61]
# b = [2293, 0]
# c = [60, 0, 0, 5]
#
#
# for strok in range(9):
#         str_a = "".join(map(str, s))
#         str_b = "".join(map(str, b))
#         str_c = "".join(map(str, c))
#         int_a = int(str_a, 21)
#         int_b = int(str_b, 17)
#         int_c = int(str_c, 15)
#
#         if int_c + int_b == int_a:
#             print(strok)
#             print(s[1])
#         else:
#             s[1] += 1
#             b[1] += 1
#             c[1] += 1
#
#
# str_a = '19061'
# int_a = int(str_a, 21)
# print(int_a)
# print(str_c, str_b, str_a)
#------------------------------------------------------------------------------------------

# Максимальная сумма последовательности элементов массива
# s = list(map(int, input().split()))
# b = int(input())
# best = 0
#
# for strok in range(len(s) - b + 1):
#     if best <= s[strok] + s[strok + 1]:
#         best = s[strok] + s[strok + 1]
# print(best)
# s.sort()
# s = s[::-1]
# s = s[:b]
#
# print(sum(s))
#
#
# for strok in range(b):
#     for h in s:
#         summ = s[h] + s[h + 1]
#
# print(summ)
#------------------------------------------------------------------------------------------
# Строго возрастающая последовательность
# s = list(map(int, input().split()))
# length = 0
#
# for strok in range(len(s) - 1):
#     if s[strok]  < s[strok + 1]:
#         continue
#     elif s[strok]  == s[strok + 1]:
#         length += 1
#     elif len(s) > len(set(s)):
#         length += 1
#     else:
#         length += 1
# if length <= 1:
#     print('true')
# else:
#     print('false')

#------------------------------------------------------------------------------------------
#
# Выращивание растений
# upSpeed = int(input())
# downSpeed = int(input())
# desiredHeight = int(input())
# length = 0
# height = 0
# while True:
#     height += upSpeed
#     length += 1
#     if height >= desiredHeight:
#         break
#     height -= downSpeed
#
# print(length)

#------------------------------------------------------------------------------------------
# n = int(input())
# p = 2
# strok = 0
# c = 2
# s = []
# if strok < n:
#     s[strok] = strok + 2
#     strok += 1
#------------------------------------------------------------------------------------------
# Максимальная сумма последовательности элементов массива
s = list(map(int, input().split()))
b = int(input())
# best =

for strok in range(len(s) - b + 1):
	if best is None or best < sum(s[strok : strok + b]):
		best = sum(s[strok : strok + b])
print(best)

s = s[::-1]
s = s[:b]

print(sum(s))

#
# for strok in range(b):
#     for h in s:
#         summ = s[h] + s[h + 1]
#
# print(summ)
#------------------------------------------------------------------------------------------
# a = list(map(int, input().split()))
# c = True
# for i in range(len(a) - 1):
#     if c:
#         for j in range(len(a) - 1 - i):
#             if a[j] > a[j + 1]:
#                 a.remove(a[j])
#                 c = False
#                 break
# if (len(a) == len(set(a))) and a == sorted(a):
#     print('true')
# else:
#     print('false')




# import copy
#
# s = list(map(int, input().split()))
# d = copy.copy(s)
# d.sort()
# length = 0
#
#
# for i in range(0, len(d) - 1):
#     if d[i] == d[i + 1]:
#         length += 1
#
#
# for strok in range(len(s) - 1):
#     if s[strok]  < s[strok + 1]:
#         continue
#     elif s[strok]  == s[strok + 1]:
#         length += 1
#     elif s[strok] > s[strok + 1]:
#         length += 1
#     elif s[strok] in temp_s:
#         length += 1
# if length <= 1:
#     print('true')
# else:
#     print('false')
#
#
# s = list(map(int, input().split()))
# b = True
# for i in range(len(s) - 1):
#     if b:
#         for j in range(len(s) - 1 - i):
#             if s[j] > s[j + 1]:
#                 s.remove(s[j])
#                 b = False
#                 break
# if (len(s) == len(set(s))) and s == sorted(s):
#     print('true')
# else:
#     print('false')
#------------------------------------------------------------------------------------------
# first task
# import itertools
#
# count = 0
# for item in itertools.permutations("ddttttcccc"):
#     s = "".join(item)
#     if "dd" in s and "tttt" in s and "cccc" in s:
#         count +=1
# print(count)
#------------------------------------------------------------------------------------------
# second task
# I = 760 * 1024 * 1024 * 8
# k = 4 * 5 * 600 * 600
# i = 24
# Ik = 8 * 1024 * 8
# Ii = i * k + Ik
# n = I // Ii
# print(n)
#------------------------------------------------------------------------------------------
# for i, el in enumerate(range(10)):
#     y1 = int(f"19{el}61", 12)
#     y2 = int(f"3393{el}", 17)
#     y3 = int(f"60{el}05", 15)
#     if y1 + y2 == y3:
#         print(el)
#------------------------------------------------------------------------------------------
# import itertools
# for item in itertools.product()
