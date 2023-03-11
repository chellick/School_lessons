# import numpy as np
#
# # n = input()
# m = [[0, 0, 0, 0],
#      [0, 0, 0, 0],
#      [0, 0, 0, 0],
#      [0, 0, 0, 0]]
#
# Answer = [[2, 5, 10, 18],
#           [3, 8, 16, 23],
#           [5, 13, 20, 24],
#           [8, 15, 19, 25]]
# strok = 0
# stolbec = 0
# constant = 4
# for n in range(10000000, 100000000):
#     while strok < constant:
#         stolbec = 0
#         while stolbec < constant:
#             k = strok
#             while k <= strok + stolbec:
#                 print(strok)
#                 m[strok][stolbec] = m[strok][stolbec] + int(str(n)[k])
#                 k += 1
#             stolbec += 1
#         strok += 1
#     print(np.array(m))
#     if m == Answer:
#         print(np.array(m))
speed = 30
length = 0
time = 1
temp = 0
while speed != 0:
    length += speed / time
    speed = speed / 1.5
    temp += 1
    print(length)
print(length)