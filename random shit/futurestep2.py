import itertools
k, d = map(int, input().split())
r = 0
strok = ''

for i in range(d):
    strok += str(i)

strok = strok[::-1]
for i in itertools.combinations(strok, 6):
    if int(''.join(i)) % k == 0:
        r += 1
print(r)
