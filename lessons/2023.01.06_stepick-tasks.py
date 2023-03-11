a = int(input())
mat = []
row = []
for i in range(a):
    for i in range(a):
        row.append(1)
    mat.append(row)
    row = []

for i in range(1):
    for j in range(a):
        mat[i][j] += j

for i in range(1, a):
    for j in range(1, 2):
        mat[i][-j] += i + a - 1

for i in range(1):
    for j in range(a):
        mat[-1][j] = j + a * 2 - 1

mat[-1] = mat[-1][::-1]

for i in range(1, a - 1):
    for j in range(1):
        mat[-i - 1][j] = a * 3 + i - 2

for i in range(1):
    for j in range(a - 2):
        mat[i + 1][j + 1] += a * 4 + j - 4

for i in range(2, a - 1):
    for j in range(2, 3):
        mat[i][-j] = mat[i - 1][-j] + 1

for i in range(1):
    for j in range(1, a - 2):
        mat[-2][j] = mat[-2][-2] + j



for i in range(a):
    print(*mat[i], sep='\t')




# a = [0, 0, 0, 0, 0]
# for i in range(len(a)):
#     a[i] += 1 + i
# print(a)