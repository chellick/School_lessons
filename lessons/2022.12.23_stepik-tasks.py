# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# mat = []
# row = []
# for i in range(a, b + 1):
#     for j in range(c, d + 1):
#         row.append(0)
#     mat.append(row)
#     row = []
# print(mat)
#-------------------------------------------------
# a = int(input())
# b = int(input())
# c = []
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         c.append(i)
# print(sum(c) / len(c))
#-------------------------------------------------
# s = input()
# counter = 0
# a = []
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         counter += 1
#     else:
#         a.append(counter)

#-------------------------------------------------
# def points(games):
#     count = 0
#     for i in games:
#         if int(i[0]) == int(i[-1]):
#             count += 1
#         elif int(i[0]) > int(i[-1]):
#             count += 3
#         elif int(i[0]) < int(i[-1]):
#             continue
#
#     return count
# print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
#-------------------------------------------------

# def find_outlier(integers):
#     even = []
#     odd = []
#
#
#     for i in range(len(integers)):
#         if integers[i] % 2 == 0:
#             even.append(integers[i])
#         else:
#             odd.append(integers[i])
#
#     if len(odd) < len(even):
#         return odd[0]
#     else:
#         return even[0]
#
# print(find_outlier([2, 4, 6, 8, 10, 3]))

#-------------------------------------------------
# def get_sum(a, b):
#     summ = 0
#     s = [a, b]
#
#     for i in range(min(s), max(s) + 1):
#         summ += i
#
#     return summ
#
# print(get_sum(0,-1))
#-------------------------------------------------
# def get_min_base(number):
#     res = ''
#     sis = 2
#     x = number
#     while True:
#         while x > 0:
#             res = str(x % sis) + res
#             x = x // sis
#
#         if len(set(res)) == 1 and int(res[0]) == 1:
#             return sis
#         else:
#             sis += 1
#         x = number
#         res = ''
# print(get_min_base(1111))


# n = int(input())
# sis = int(input())
# res = ''
# while n > 0:
#     res = str(n % sis) + res
#     n = n // sis
# print(res)
def get_min_base(number):
    res = ''
    sis = 2
    x = number
    while True:
        while x > 0:
            res = str(x % sis) + res
            x = x // sis
            if x % sis == 0:
                sis += 1
                continue

        if len(set(res)) == 1 and int(res[0]) == 1:
            return sis - 1

        x = number
        res = ''
print(get_min_base(21))