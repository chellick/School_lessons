def matrix(a, b, c):
    return [[c for _ in range(b)] for _ in range(a)]

print(matrix(2, 3, 'X'))


def carpet(r, c, a, b):
    row = []
    for _ in range(c):
        row.append(