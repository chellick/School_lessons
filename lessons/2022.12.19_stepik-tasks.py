#------------------------------------------------------------------------------

"""
s = list(map(int, input().split()))
a = int(input())

temp = []
count = 0

for i in range(len(s)):
    if a == s[i]:
        temp.append(i)
        count += 1

tempstr = " ".join(str(my_tuple) for my_tuple in temp)
if count == 0:
    print('Отсутствует')
elif count != 0:
    print(tempstr)
"""

#------------------------------------------------------------------------------

"""
s = list(map(int, input().split()))
summ = []
for i in range(len(s) - 1):
    summ.append(s[i] + s[i + 1])
m = " ".join(str(el) for el in summ)
print(m)
"""

#------------------------------------------------------------------------------
"""
s = list(map(int, input().split()))
a = []
s.sort()

for i in s:
    if s.count(i) > 1:
        a.append(i)

a = set(a)

m = " ".join(str(el) for el in a)
print(m)
"""

#------------------------------------------------------------------------------

"""
a = str(input())
a = a.lower()
count_g = a.count('g')
count_c = a.count('c')
count = count_c + count_g
print((count / len(a)) * 100)
"""

#------------------------------------------------------------------------------

s = 'abcdefghijk'
print(s[3:6],
        s[:6],
        s[3:],
        s[::-1],
        s[-3:],
        s[:-6],
        s[-1:-10:-2])