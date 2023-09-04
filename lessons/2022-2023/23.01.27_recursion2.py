# import sys
# from functools import lru_cache

# sys.setrecursionlimit(10000)



# cache = dict()
# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n-1) * n
#
# # for i in range(1, 20+1):
# #     fac(i)
#
# def c(n, k):
#     return fac(n) / (fac(k) * fac(n - k))
# print(c(3, 30))
# # print(fac(5))


# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 2:
#         return f(n - 1) + 1
#     if n > 0 and n % 3 < 2:
#         return f((n - (n % 3)) / 3)
#
# for i in range(0, 1000000):
#     if f(i) == 5:
#         print(i)  # 242



# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n - 1)
# print(f(2023) / f(2020))  # 8266912626.0


# def f(n):
#     if n < 3:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return f(n - 2) + f(n - 1) - n
#     if n > 2 and n % 2 != 0:
#         return f(n - 1) - f(n - 2) + 2 * n
#
# print(f(32))

#
# s = int(input())
# count = 0
# def t(n):
#     global s
#     global count
#
#     if n == 0:
#         return 0
#     if s == n % 10 + t(int(n / 10)):
#         count += 1
#     return count
#
# print(t(10101))

# count = 0
# s = int(input())
# def f(n):
#     global s
#     global count
#     if t(n) == s:
#         count += 1
#     n = t(n + 1)
#     return count
#
# print(f(50000))

# def f(n):
#     if n <= 2:
#         return 1
#     if n == 2:
#         return 2
#     return n + f(n - 3) + f(n - 42)
#
# print(f(2023) + f(2021) - 2 * f(213))
# print(1)
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n <= 2:
#         return 1
#     if n == 2:
#         return 2
#     return n + f(n - 3) + f(n - 42)
# for i in range (2,2023):
#     f(i)

# x=f(2023) + f(2021) - 2 * f(213)
# print(sum(map(int,list(str(x)))))


lst = []

def f(x, res):
    lst.append(res)
    return f(x + 1, res) + f(x + 2, res) + f(x * 2, res)


print(f(1, 11))