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




def algo(n):
    r = bin(n)[2:]
    if n % 4 == 0:
        r += r[-2:]
    
    else:
        r = bin((n % 4) * 2)[2:] + r
    return int(r, 2)
 
for n in range(3, 1000):
    r = algo(n)
    if r < 68:

        print(n)
        
    
def algo(n):
    r = bin(n)[2:].zfill(8)
    r = r[:2] + r[-2:]
    return int(r, 2)

for n in range(131, 1000):
    if algo(n) == 10:
        print(n, algo(n))
        break
 

def algo(n):
    r = bin(n)[2:]
    if r.count("1") % 2 == 0:
        r = '1' + r + '00'
    else:
        r = '11' + r
    return int(r, 2)

print(algo(13), algo(12))

minimum = 100000
for n in range(1, 1000):
    r = algo(n)
    if r >= 412:
        if minimum > n:
            minimum = n
            print(n, r)
print(minimum)



def algo(n):
    n = [int(i) for i in str(n)]
    num1 = n[0] + n[1]
    num2 = n[1] + n[2]
    num3 = n[2] + n[3]
    r  = "".join(sorted([str(num1), str(num2), str(num3)])[1:])
    
    return int(r)

print(algo(1000))

for n in range(10000, 999, -1):
    r = algo(n)
    if r == 1517:
        print(n)
        
# print(algo(9575))


def algo(n):
    n = list(sorted([int(i) for i in str(n)], reverse=True))
    num = int(str(n[0]) + str(n[1])) - int(str(n[-1]) + str(n[-2]))
    return num


c = 0
for i in range(800, 901):
    if algo(i) == 30:
        c += 1
        
print(c)


def algo(n):
    n = [int(i) for i in str(n)]
    n = [bin(i)[2:].zfill(4) for i in n]
    m = []
    for i in "".join(n):
        if i == "0":
            m.append("1")
        else:
            m.append("0")
            
    return int("".join(m), 2)

for n in range(1, 1000):
    if algo(n) == 151:
        print(n)
        break


"""  
def algo(n):
    bin_n = bin(n)[2:]
    bin_n += bin(n % 3)[2:4].zfill(2)
    bin_n += bin(int(bin_n, 2) % 5)[2:5].zfill(3)
    return int(bin_n, 2)


c = 0

for n in range(38000000, 49000000):
    if 1222222222 <= algo(n) <= 1555555666:
        c+=1
        
print(c)