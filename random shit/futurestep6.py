n = int(input())
x = int(input())
max_pave = int(input())
c = []
summa = 0
count = 0
for i in range(n):
    b = int(input())
    c.append(b)
c.sort()
for el in c:
    if max_pave - el >= 0:
        summa += el
        count += 1
        max_pave -= el
    else:
        break
if count == x:
    print(summa)
else:
    print(0)
    