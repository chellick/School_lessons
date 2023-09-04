#-------------------- Двоичные числа длиной 6 ------------------------
# b = []
# c = []
# for i in range(31):
#     b.append(i)
#     i += 1
# # print(b)
# for i in b:
#     c.append(bin(i))
# print(c)
#-------------------- Двоичные числа длиной 6 ------------------------
# import itertools
# for el in itertools.product("01", repeat=6):
#     print("".join(el))
#---------------------------------------------------------------------
"""`
el = df.iloc[0:100, [0, 2]].values
y = np.where(y == 'sd', -1, 1)
"""
#-------------- Сколько слов начинается с согласного -----------------
# import itertools
# count = 0
# for el in itertools.product("ГОД", repeat=6):
#     s = "".join(el)
#     if s[0] == 'Г' or  s[0] == 'Д':     # if el[0] in "ГД":
#         count += 1
# print(count)
#--- Слова длины 4 с началом на согласную и окончанием на гласную ----
# import itertools
# count = 0
# for el in itertools.product("МЕТРО", repeat=4):
#     s = "".join(el)
#     if el[0] in "МТР" and el[-1] in "ЕО":     # if el[0] in "ГД":
#         count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.product("ЛЕВИЙ", repeat=5):
#     s = "".join(el)
#     for i in s:
#         if i != i + 1 and s[0] != 'Й' and  (s[i] + s[i + 1]) not in "ЕИ":
#             count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.product("ЛЕВИЙ", repeat=5):
#     s = "".join(el)
#     if el.count('Л') == 1 and el.count('Е') == 1 and el.count('В') == 1 and el.count('И') == 1 and el.count('Й') == 1:
#         if el[0] != 'Й'  and  'ЕИ' not in "".join(el):
#             count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.permutations("ЛЕВИЙ"):
#     s = "".join(el)
#     if el[0] != 'Й'  and  'ЕИ' not in "".join(el):
#         count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.permutations("МАТВЕЙ"):
#     s = "".join(el)
#     if el[0] != 'Й'  and  'АЕ' not in "".join(el):
#         count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# glas1 =[]
# sogl1 = []
# for el in itertools.permutations("ГЕРАСИМ"):
#     s = "".join(el)
#     for b in itertools.product("ЕАИ", repeat=2):
#         glas = "".join(b)
#         glas1.append(glas)
#
#     for n in itertools.product("ГРСМ", repeat=2):
#         soglas = "".join(n)
#         sogl1.append(soglas)
#
#     for i, b in zip(glas1, sogl1):
#         if i not in s and b not in s:
#             count += 1
# print(count)
#-------------------- Гласные \ согласные буквы ----------------------
# import itertools
# count = 0
# for el in itertools.permutations("ГЕГЕГЕГ"):
#     s = "".join(el)
#     if "ГГ" not in s and "ЕЕ" not in s:
#         count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.permutations("АЛЬГА"):
#     s = "".join(el)
#     if "Ь" not in s[0] and "АЬ" not in s:
#         count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# sogl = ['Р', 'С', 'М', 'Х']
# glas = ['О', 'А']
# for el in itertools.permutations("РОСОМАХА"):
#     s = "".join(el)
#     for i in range
#     if not(s[i] in glass and s[i + 1] in glass) and not(s[i] in soglas and s[i + 1] in soglas):
#         count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
#
# for el in itertools.permutations("ГЕОРГИЙ"):
#     s = "".join(el)
#     if "ГГ" not in s and "ЕЕ" not in s:
#         count += 1
# print(count / 2)
#
# lst = list(itertools.permutations("ГЕОРГИЙ"))
# srt = lst.count(("Г", "Е", "О", "Р", "Г", "И", "Й"))
# print(srt)
#---------------------------------------------------------------------
# import itertools
# count = 0
#
# lst = list(itertools.permutations("ГЕПАРД"))
# srt = lst.count(("Г", "Е", "П", "А", "Р", "Д"))
# print(srt)
#
# for el in itertools.product("ГЕПАРД", repeat=5):
#     s = "".join(el)
#     if s[0] != 'А' and s[-1] != 'Е':
#
#         count += 1
# print(count / 2)
#---------------------------------------------------------------------
# import itertools
# lst = list(itertools.permutations("1234567"))
# srt = lst.count(("1", "2", "3", "4", "5", "6", "7"))
# count = 0
# for el in itertools.product('1234567', repeat = 5):
#     s = "".join(el)
#     temp_count = s.count('6')
#     if 0 < temp_count < 2:
#         temp_index = s.index('6')
#
#     if temp_index > 5:
#         temp_count > 0 and int(s[temp_index - 1]) % 2 == 0:
#
#     if temp_index < 5:
#          if s[temp_index + 1] % 2 == 0:
#             count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.product('01234567', repeat = 5):
#     s = "".join(el)
#     if s.count('6') != 1:
#         continue
#     if s[0] == '0':
#         continue
#     if s.count('6') == 1:
#         temp_index = s.index('6')
#     if 0 < temp_index < 4:
#         if int(s[temp_index - 1]) % 2 == 0 and int(s[temp_index + 1]) % 2 == 0:
#             count += 1
#     if temp_index == 0:
#         if int(s[temp_index + 1]) % 2 == 0:
#             count += 1
#     if temp_index == 4:
#         if int(s[temp_index - 1]) % 2 == 0:
#             count += 1
# print(count)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.product('АОУ', repeat = 5):
#     s = "".join(el)
#     count += 1
#     if count == 210:
#         print(s)
#---------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.product('АВОРТ', repeat = 4):
#     s = "".join(el)
#     count += 1
#     if 'ВАТА' in s:
#         print(count, s)
#--------------------------------------------------------------------
# import itertools
# count = 1
# for el in itertools.product('АБРТЫ', repeat = 5):
#     s = "".join(el)
#     if s.count('Ы') == 0:
#         if 'АА' not in s:
#             print(count)
#     count += 1
#--------------------------------------------------------------------
# import itertools
# count = 0
# for el in itertools.product('1234', repeat = 5):
#     s = "".join(el)
#     if s.count('1') == 2:
#         count += 1
# print(count)
#--------------------------------------------------------------------
# el = bin(4 ** 2020 + 2 ** 2017 - 15)[2:].count('1')
# print(el)
#--------------------------------------------------------------------

