
# 100 первых простых чисел

d = dict()


def prost(x):
     s = []
     i = 1
     while len(s) != x:
          count = 0
          for n in s:
               if i % n == 0:
                    count += 1
          if count <= 1:
               s.append(i)
          i += 1
     return s


for v in prost(100):
     d[v] = v * 2
print(d)

# for strok, (k, v) in enumerate(d):
#      print(strok, v)



# d = {'albert' : 'alimov',
#      'archip' : 'msokovskiy'
#      }

# print(d[''])
# m = [1, 2, 3, 4, 5, 6]
# print(m[0])

     



