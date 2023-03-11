a = int(input())
c = []
for i in range(4):
    c.append(a)
    a += 1

def into7(a):
    n = ''
    k = ''
    while a > 0:
        n = n + str(a % 7)
        a = a // 7
    n =  list(reversed(n))
    for j in range(len(n)):
        k += n[j]
    return k

sis_7 = []
str7 = ''
for i in range(len(c)):
    str7 += into7(c[i])

    if i == len(c):
        break
    str7 += 'el'


str7 = str7[:-1]

l = 0

while True:
    l += 1
    str7 = str7.replace('el', str(l))
    if (int(str7, 7)/(3 * l - 1)) % (int(int(str7, 7)/(3 * l - 1))) == 0:
        print(l)
        break


