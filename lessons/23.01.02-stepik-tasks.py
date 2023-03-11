"""
s = input()
m = []
for i in range(len(s)):
    m.append(s[i])
for i in range(len(s) - 1):
    if m[i] == m[i + 1]:
        m[i] = m[i] + m[i + 1]
        del m[i + 1]
    if m[i + 1] is None or i + 1 == len(s):
        break

print(m)

s = []
count = 0
for i in range(100):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count <= 2:
        s.append(i)
    count = 0
for i in s:
    print(i, end=' ')


a = int(input())
if 9 < a % 100 < 21 or a % 10 == 0 or 4 < a % 10 < 10:
    print(a, 'программистов')
elif a % 10 == 1:
    print(a, 'программист')
elif 1 < a % 10 < 5:
    print(a, 'программиста')



import numpy as np
h1 = int(input())
h2 = int(input())
lim1 = int(input())
lim2 = int(input())


def mult_table(n):
    rng = np.arange(1, n+1)
    return rng * rng[:, None]


mat = mult_table(10)

print(mat[h1 - 1:h2, lim1 - 1:lim2])

print(i for i in range(lim1, lim2 + 1))
"""
# import numpy as np
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(type(a))
