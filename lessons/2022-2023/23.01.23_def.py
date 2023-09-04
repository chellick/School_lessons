# def f(n):
#     if n == 0:
#         return 1
#     res = n * f(n - 1)
#     return res
# print(f(5))

# def g(a, b):
#     if b == 0:
#         return a
#     res = g(a, b - 1) + 1
#     return res
# print(g(5, 3))

# def f(n):
#     print(n)
#     if n < 5:
#         f(n + 1)
#         f(n + 3)
# print(f(1))



def f(n):
    if n > 20:
        print(n - 1, end=' ')
        f(n - 9)
    if n > 3:
        f(n - 5)
f(45)