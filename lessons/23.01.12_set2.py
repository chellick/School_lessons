# a = {1, 3, 4}
# b = {5, 3, 8}
# c = a.intersection(b)
# print(a, b, c)
# print(a.union(b))
# print(a.symmetric_difference(b))
# print(a.__xor__(b))
#
#
#
# a = int(input())
# b = int(input())
#
# s1 = set()
# s2 = set()
#
# for i in range(a):
#     m = input()
#     s1.add(m)
#
#
# for i in range(b):
#     n = input()
#     s2.add(n)
#
# s3 = s1.symmetric_difference(s2)
# if len(s3) != 0:
#     print(len(s3))
# else:
#     print('NO')
#
# a = int(input())
# b = int(input())
# c = []
# for i in range(a + b):
#     m = input()
#     c.append(m)
#
# if len(set(c)) * 2 == len(c):
#     print('NO')
# else:
#     print(len(set(c)))
#
# a = set(list(map(int, input().split())))
# b = set(list(map(int, input().split())))
# print(len(a.intersection(b)))
#
# m, n = map(int, input().split())
#
# a = set(list(map(int, input().split())))
# b = set(list(map(int, input().split())))
# for i in a.intersection(b):
# 	print(i, end=' ')


# a, b = map(int, input().split())
#
# s1 = list(map(str, input().split()) for _ in range(a))
# print(s1)
# s2 = list(map(str, input().split()))
#
#
# # print(c)
#
# for j in s1:
#     if j in s2:
#         print('Yes')
#     else:
#         print('No')


# a, b = map(int, input().split())
#
# s = []
# for i in range(a):
#     s.append(input().split())
# print(s)


# a = list(map(int, input().split()))
# b = []
# for i in a:
#     if i in b:
#         print('YES')
#     else:
#         print('NO')
#     b.append(i)


# a = int(input())
# s = set()
# for i in range(a):
#     n = input()
#     if '+' == n[0]:
#         s.add(n[-1])
#     elif '-' == n[0]:
#         s.remove(n[-1])
#
# if len(s) != 0:
#     for i in s:
#         print(i, end=' ')
# else:
#     print(-1)

a, b = map(int, input().split())
s = []
for i in range(a):
    s.append(input().split())

s_sets = []
for i in s:
    s_sets.append(set(i))

a = list(set.intersection(*s_sets))
sorted(a)

if len(a) > 0:
    for i in a:
        print(i, end=' ')
else:
    print(-1)
