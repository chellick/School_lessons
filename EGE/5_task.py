"""
# 8094
for n in range(1, 1000):
    bin_n = bin(n)[2:]
    for i in range(2):        
        summa = bin_n.count('1')
        bin_n += str(summa % 2)
    
    
    r = int(bin_n, 2)
    if r > 43:
        print(r)
        break
    
    

# 15622
for n in range(1, 1000):
    bin_n = bin(n)[2:]

    if bin_n.count('1') % 2 == 0:
        bin_n += '00'

    elif bin_n.count('1') % 2 == 1:
        bin_n += '11'

    r = int(bin_n, 2)
    
    if r > 114:
        print(r)
        break


# 45239
for n in range(1, 1000):
        
    bin_n = bin(n)[2:]

    if n % 2 == 0:
        bin_n = '10' + bin_n

    elif n % 2 == 1:
        bin_n = '1' + bin_n + '01'
        
    r = int(bin_n, 2)
    
    if r > 441:
        print(n)
        break
    
        

# 55801
for n in range(1, 1000):
    bin_n = bin(n)[2:]

    if n % 3 == 0:
        bin_n += bin_n[-3:] 
        
    elif n % 3:
        bin_n += bin(n % 3 * 3)[2:]

    r = int(bin_n, 2)

    if r < 100:
        print(n, r)
  

# 57412
for n in range(1, 1000):
    bin_n = bin(n)[2:]
    
    if n % 3 == 0:
        bin_n += bin_n[-3:]
        
    else:
        bin_n += bin(n % 3 * 3)[2:]
        

    r = int(bin_n, 2)
    
    if r >= 76:
        print(n)
        break
    


# 15101
for i in range(1000, 10000):
    i = str(i)
    l = []
    l.append(int(i[0]) + int(i[1]))
    l.append(int(i[1]) + int(i[2]))
    l.append(int(i[2]) + int(i[3]))
    
    l = sorted(l)
    
    summa = str(l[1]) + str(l[2])
    
    if summa == '1215':
        print(i)
    
  

# 11342
for i in range(100, 1000):
    i = str(i)
    l = []
    l.append(int(i[0]) + int(i[1]))
    l.append(int(i[1]) + int(i[2]))
    
    l = sorted(l, reverse=True)
    summa = str(l[0]) + str(l[1])
    
    if summa == '1711':
        print(i)
        


# 5899
import itertools


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def double(num):
    listik = itertools.permutations(str(num), 2)
    result = set(int(''.join(i)) for i in listik)
    return result

max_n = 0
max_primes = 0


for n in range(100, 1000):
    temp_max_primes = 0 
    for i in double(n):
        temp_max_primes += is_prime(i)
    if temp_max_primes >= max_primes:
        max_primes = temp_max_primes
        max_n = n
        

print(max_n, max_primes)
"""  

"""
def algo(n):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += bin((n%3)*3)[2:]
    return int(bin_n, 2)


for i in range(4, 1000):
    if algo(i) <= 170:
        print(i , algo(i))

maxi = 0
for n in range(4, 1000):
    
    s = bin(n)[2:] # перевод в двоичную систему
    if n % 3 == 0:
        s += bin(n)[-3:]
    else:
        s += bin((n%3)*3)[2:]
    r = int(s,2)
    
    if r < 170 and r > maxi:
        maxi = r
        print(n)
print(maxi)
"""