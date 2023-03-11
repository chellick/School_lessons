a = int(input())
count = 0
c = []
for i in range(a):
    b = int(input())
    c.append(b)
# print(c)
for i in range(len(c)):
    if i == len(c) - 1:
        break

    if c[i] < c[i + 1]:
        count += 1

print(count)
# print(c)