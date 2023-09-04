# import sys
#
# # sys.setrecursionlimit(5000)
#
# cache = dict()
#
#
# def f(n):
#     if n in cache:
#         return cache[n]
#     if n == 1:
#         res = 1
#         cache[n] = res
#         return res
#     if n == 2:
#         res = 2
#         cache[n] = res
#         return res
#
#     if n > 2:
#         res = n * (n - 1) + f(n - 1) + f(n - 2)
#         cache[n] = res
#     return res
#
# for i in range(1, 2023 + 1):
#     f(i)
#
# print(f(2023) - f(2021) - 2 * f(2020) - f(2019))


# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n - 1)
#
#
# l = int(input())
# print(fac(l))


