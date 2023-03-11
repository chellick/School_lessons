count = 0
n = int(input())
for i in range(n):
    s = str(input())
    summ = sum(list(map(int, str(int(s, 16)))))
    summ_5 = ''
    while summ > 0:
        summ_5 += str(summ % 5)
        summ //= 5
    if summ_5[::-1][-1] == '0':
        count += 1

print(count)