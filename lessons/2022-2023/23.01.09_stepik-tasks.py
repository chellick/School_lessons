# from time import sleep
# c = 0
# p = ['/', '-', '|', '\\']
# for i in range(100 + 1):
#
#     s = p[c]
#     c += 1
#
#     print(f'\r[{s}] {i}%', end="")
#
#     sleep(0.05)
#     if c == 3:
#         c = 0
#
"""
s = list(map(int, input().split()))
height = max(s) + 2
width = len(s) + 2

mat = []
row = []
for i in range(height):
    for j in range(width):
        row.append('0')
    mat.append(row)
    row = []
print(mat)
"""


m = list(map(str, input().split()))
lstint = []
for i in m:
    if i.lstrip('-').isdigit():
        lstint.append(int(i))

    else:

        num1 = lstint.pop()
        num2 = lstint.pop()
        if i == '+':
            lstint.append(num1 + num2)
        elif i == '-':
            lstint.append(num1 - num2)
        elif i == '*':
            lstint.append(num1 * num2)
        elif i == '/':
            lstint.append(num1 / num2)
        elif i == '**':
            lstint.append(num1 ** num2)


print(lstint)
# print(1 + 1)

"""
1 2 +
2 + 1



1 2 3 + *
3 + 2 = 5
5 * 1 = 5


3 4 *
4 * 3 = 12

1 2 4 + *
1 6 *
4 + 2 = 6
6 * 1 = 6


2 3 + 3 *
3 + 2 = 5
3 * 5 = 15


5 3 - 5 * 3 *
"""



# 3 9 + 1 / 1 + 1 / 1 + 1 / 1 + 3 5 3 6 5 - * * * /   6 5 / 6 * 6 - 3 ** 2 + 6 +