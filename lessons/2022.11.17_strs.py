
# c = "Из-за экономичкеской игры занятий сегодня не будет"
# c = c.replace('экономической игры' , 'ЭКОНОМИЧЕСКОЙ ИГРЫ')
# print(c)

# s =  '12 45'
# s = s.replace(' ', '')
# b = s[:2:]
# c = s[2::]
# b = int(b)
# c = int(c)
# print(b + c)
a = "12+45+85+42"

a = a.replace('+', ' ')
a = a.split()
c = 0
# print(int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]))
for i in a:
     c += int(i)
print(c)