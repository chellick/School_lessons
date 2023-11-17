"""
# 9365
stroka = "8" * 68

while "222" in stroka or "888" in stroka:
    if "222" in stroka:
        stroka = stroka.replace("222", "8", 1)
        
    else:
        stroka = stroka.replace("888", "2", 1)
    
print(stroka)


stroka = "2" + "9" * 100

while "19" in stroka or "299" in stroka or "3999" in stroka:
    stroka = stroka.replace("19", "2", 1)
    stroka = stroka.replace("299", "3", 1)
    stroka = stroka.replace("3999", "1", 1)
    
print(stroka)



# 23912

stroka = ">" + "1" * 10 + "2" * 20 + "3" * 30

while ">1" in stroka or ">2" in stroka or ">3" in stroka:
    if ">1" in stroka:
        stroka = stroka.replace(">1", "22>", 1)
    
    if ">2" in stroka:
        stroka = stroka.replace(">2", "2>", 1)
        
    if ">3" in stroka:
        stroka = stroka.replace(">3", "1>", 1)

summ = 0


print(sum([int(i) for i in stroka.replace(">", "")]))


# 27240
import itertools


stroka = "12"
maximum = 0
best = None


for j in itertools.product(stroka, repeat=13):
    j = "".join(j)
    if j.count("1") == 10 and j.count("2") == 3:
        while "11" in j:
            if "112" in j:
                j = j.replace("112", "6")
            
            else:
                j = j.replace("11", "3")
        
        if maximum < sum([int(i) for i in j]):
            maximum = sum([int(i) for i in j])
            best = j

print(maximum, best)


# 27299

for i in range(61, 1000, 1):
    stroka = "1" * i
    
    while "111" in stroka:
        stroka = stroka.replace("111", "2", 1)
        stroka = stroka.replace("222", "11", 1)
    
    if "221" == stroka:
        print(i)
        break  

# 35986
def algorythm(stroka:str):
    while "00" not in stroka:
        stroka = stroka.replace("01", "210", 1)
        stroka = stroka.replace("02", "320", 1)
        stroka = stroka.replace("03", "3012", 1)
    return stroka

def check(stroka:str):
    return stroka.count("1") == 23 and\
            stroka.count("2") == 48 and\
                stroka.count("3") == 41
    

for i in range(1, 100):
    for j in range(1, 100):
        for l in range(1, 100):
            stroka = "0"+ "1" * i + "2" * j + "3" * l + "0"
            if check(algorythm(stroka)):
                print(len(stroka))      
          
# 39241

def algorithm(stroka:str):
    while "111" in stroka or "222" in stroka:
        stroka = stroka.replace("111", "22", 1)
        stroka = stroka.replace("222", "1", 1)
    return stroka
    
for i in range(201, 1000):
    stroka = "1" * i
    stroka = algorithm(stroka)
    if stroka.count("1") == 0:
        print(i)
        break
 
    
def algorithm(stroka:str):
    while "1111" in stroka:
        stroka = stroka.replace("1111", "22", 1)
        stroka = stroka.replace("222", "1", 1)
    
    return stroka
            
minimum = 100000

for i in range(201, 1000):
    stroka = algorithm("1" * i)
    
    if minimum > stroka.count("1"):
        minimum = stroka.count("1")
        best = i

print(best)

# 5062
import itertools


def alg(stroka:str):
    while "00" not in stroka:
        stroka = stroka.replace("011", "20", 1)
        stroka = stroka.replace("022", "10", 1)
        stroka = stroka.replace("02", "110", 1)
        stroka = stroka.replace("01", "220", 1)
    return stroka

def check(stroka:str):
    if stroka.count("1") == 47:
        return stroka.count("2")

maximum = 0

for j in range(50):
    for i in itertools.product("012", repeat=j):
        i = "".join(i)
        
        if i[0] == "0" and i[-1] == "0" and i.count("2") == i.count("1"):
            i = alg(i)
            i = check(i)


def r(s):
    while '56' in s or '1111' in  s:
        s = s.replace('56', '1', 1)
        s = s.replace('1111', '1', 1)
    return s

print(r('561' * 102))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]


import itertools
def algo(s):
    while "01" in s or "02" in s:
        s = s.replace("02", "1110", 1)
        s = s.replace("01", "220", 1)
    return sum([int(i) for i in s])

s = "012"
for times in range(40, 50):
    for i in itertools.product(s, repeat=times):
        print("".join(i))
        if algo("".join(i)) in primes:
            print("".join(i), times, algo("".join(i)))

"""
