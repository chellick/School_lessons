
import itertools
"""
# 1
counter = 0

for i in itertools.product('ЕГЭ', repeat=5):
    if i[0] == 'Е' or i[0] == 'Э': 
        counter += 1
        
        
print(counter)

# 26982
counter = 0

def to_num(digits):
    return int(''.join(digits))

def check_tuple(digits):
    for i in range(len(digits)-1):
        if (int(digits[i]) % 2 == 0 and int(digits[i+1]) % 2 == 0) or\
            (int(digits[i]) % 2 == 1 and int(digits[i+1]) % 2 == 1):
                return False
    return True

def check(digits):
    num = to_num(digits)
    if (num % 5 == 0) and check_tuple(digits):
        return True
    return False

counter = 0

for i in itertools.permutations('1234567890', 6):
    if i[0] != '0':
        if check(i) == True:
            counter += 1

print(counter)

# 28685

counter = 0


for i in itertools.product('ПЕТЯ', repeat=6):
    i = "".join(i)
    if 'ЕЯ' in i or 'ПТ' in i or 'ЯЕ' in i or 'ТП' in i or 'ТТ' in i or 'ПП' in i or 'ЯЯ' in i or 'ЕЕ' in i:
        pass
    else:
        counter += 1
        print(i)

print(counter)
  

counter = 0

for i in itertools.product('ВИШНЯ', repeat=6):
    if i.count('В') < 2 and i[0] != 'Ш' and i[-1] not in 'ИЯ':
        counter +=1 
        
print(counter)
  


def check(num):
    odd_counter = 0  
    for i in num:
        odd_counter += int(i) % 2           
    return odd_counter == 2

counter = 0

for i in itertools.product('012345678', repeat=6):
    if i.count('4') == 1 and i[0] != '0':
        counter += check(i)
    
print(counter)        

counter = 0

for i in itertools.product('КЛРТ', repeat=4):
    strok = "".join(i)
    counter += 1
    if counter == 67:
        print(strok)
        

counter = 0

for i in itertools.product(sorted('ПАРУС'), repeat=3):
    counter += 1
    if i[0] == 'С':
        print(counter)

counter = 1
for i in itertools.product(sorted('МАНГУСТ'), repeat=6):

    if i[0] != 'У' and i.count('М') == 2 and i.count('Г') < 2:
        print(counter)
    counter += 1
        


counter = 0

for i in itertools.product('КОНФЕТА', repeat=5):
    if i.count('Е') == 2 and i[1] != 'Ф':
        counter += 1
        
print(counter)
        

import time
start = time.time()


counter = 0

for i in itertools.product('CONST', repeat = 12):
    # if 'CC' not in i and 'OO' not in i and 'NN' not in i and 'SS' not in i and 'TT' not in i:
    #     if i[0] != 'S' and i[-1] != 'S':
    #         for j in range(len(i) - 2):
    #             if i[j] != i[j + 2] and i[j+1] == 'S':
    #                 counter += 1
                
                
    pass



    
# print(counter)

stop = time.time()

print(stop - start)
"""

import itertools

"""
c = 0

for i in itertools.product("110110", repeat=4):
    if i[0] == "1" and i[-1] == "0":
        c += 1
    
print(c)


c = 0

for i in itertools.product("ABC1111", repeat=6):
    i = "".join(i)

    if i[0] == "1" and i[-1] == "1" and i[1:-1].count("1") == 0:
        c += 1
        print(i, i[1:-1])
print(c)
"""
"""

c = 0

for i in itertools.product("ПУЛЯ", repeat=6):
    i = "".join(i)
    if i.count("У") == 2:
        c += 1

print(c)



s = sorted('ПАРУС')

for a, i in enumerate(itertools.product(s, repeat=4), 1):
    if i[0] == "Р":
        print(i, a)
        break
        
        


import itertools


c = 0

for i in itertools.product('WXYZ', repeat=2):
    for j in itertools.product('ABC', repeat=4):
        string = i[0] + "".join(j) + i[-1]
        c+=1
        
print(c)



a = 'МИМИКРИЯ'
c = 0



print(len(list(set((itertools.permutations(a))))))

import itertools

for a, i in enumerate(itertools.product(sorted('МАРИЯ'), repeat=4), 1):
    if a == 211:
        print(i)
        break
 
        
a = 'ПУЛЯ'
c = 0

for i in itertools.product(a, repeat=6):
    if "".join(i).count("У") == 2:
        c += 1

print(c)


a = 'ЛОДКА'
c = 0

for i in itertools.product(a, repeat=4):
    if "".join(i).count('О') >= 2:
        c += 1
        
print(c)

a = 'САЛО'
c = 0

for i in itertools.product(a, repeat=6):
    if 1 <= i.count('О') <= 3:
        c+=1
        print(i)
        
print(c)


a = 'ИГРОК'
c = 0

for i in itertools.permutations(a, r=5):
    i = "".join(i)
    if i[0] == 'К' or 'РОК' in i:
        continue
    else:
        print(i)
        c+=1
        
print(c)



a = "10101010"
c = 0

for i in itertools.permutations(a, r=8):
    i = "".join(i)
    if '00' in i or '11' in i:
        continue
    
    else:
        c += 1
        
print(c)



a = '11000'
c = 0

for i in itertools.product(a, repeat=8):
    i = "".join(i)
    if i.count('1') == 2:
        c += 1
        print(i)
    else:
        continue
    
print(c)


a = '01234'
c = 0

for i in itertools.product(a, repeat=6):
    if i[0] == '0' or i[0] == '1' or i[-1] == '3' or i[-1] == '4':
        continue
    else:
        c += 1
        
print(c)

a = '01232323'
c = 0

for i in itertools.permutations(a, r=5):
    i = "".join(i)
    if i[0] != '0' and i.count('1') == 0:
        if '22' not in i and '33' not in i and '02' not in i and '20' not in i:
            c += 1
            print(i)
            
            
print(c)



a = 'ВИШНЯ'
c = 0

for i in itertools.product(a, repeat=6):
    if i.count('В') <= 1 and i[0] != 'Ш' and i[-1] not in ('И', 'Я'):
        c+=1
        print(i)
    
print(c)


a = 'ABCD'
c = 0
s = []
for i in itertools.product(a, repeat=4):
    i = "".join(i)
    if i not in s:
        s.append("".join(sorted(i)))
    else:
        continue
        
print(s, len(set(s)))

a = 'ГЕПАРД'
c = 0
for i in itertools.product(a, repeat=5):
    if i.count('Г') == 1 and i[0] != 'А' and i[-1] != 'Е':
        c+=1
        
print(c)

a = '0123456789'
c = 0
s = []

for i in itertools.product(a, repeat=3):
    i = "".join(sorted(i))
    if i[0] != '0':
        s.append(i)

print(s, len(set(s)))

a = '01Й00001'
c = 0

for i in itertools.permutations(a, r=6):
    i = "".join(i)
    if i.count("Й") == 1:
        if 'Й0' in i:
            c += 1
            print(i)

print(c)


a = 'ВАЙФУ'
c = 0
for i in itertools.permutations(a, r=4):
    i = "".join(i)
    if i[0] != 'Й' and 'ВФ' not in i and 'ФВ' not in i:
        c += 1
        print(i)
        
print(c)



a = sorted('ЛЕМУР')
c = 0

for a, i in enumerate(itertools.product(a, repeat=4), 1):
    if i[0] == 'Л':
        print(i, a)
        break


a = sorted('АЛГОРИТМ')

for a, i in enumerate(itertools.product(a, repeat=4), 1):
    i = "".join(i)
    if i[-2:] == 'ИМ':
        print(i, a)
    



a = sorted('МАРИЯ')

for a, i in enumerate(itertools.product(a, repeat=4), 1):
    i = "".join(i)
    if 'АРИЯ' in i:
        print(i, a)
        break


word = '101010'
c = 0

for i in itertools.product(word, repeat=8):
    if i.count("1") > i.count("0"):
        c+=1
        
print(c)



import itertools

d = "КАТЕР"
c = 0

for i in itertools.product(d, repeat=6):
    if i[0] == 'Р' and i[-1] == 'К':
        c += 1
        
print(c)


d = '1010'
c = 0
for i in itertools.product(d, repeat=6):
    i = "".join(i)
    if '11' in i or '00' in i:
        continue
    print(i)
    c += 1

print(c, i)
"""

# d = sorted('РЕПЛИКА')
# c = 0

# for num, i in enumerate(itertools.product(d, repeat=6), 1):
#     if num % 2 == 0:
#         i = "".join(i) 
#         if i[0] != 'К' and i.count('И') >= 2:
#             c += 1
#             print(i, num)
            
            
# print(c)


d = '10101010'
c = 0

for i in itertools.product(d, repeat=6):
    if i.count('1') < i.count('0'):
        c += 1
        
print(c)