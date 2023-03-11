# # r = 5
# # PI = 3.14
# # s = pi * t ** 2
# # print(s)
#
# # lst = (1, 2, 3)
# # print(lst)
#
# # a, b, c = 5, 1, 9
# # n = [a, b, c]
# #
# # a = int(input())
# # s = (1, 1, 1)
# # for i in range(a - 3):
# #     s.append(sum(s[i:i + 3]))
# # # print(tuple(s))
# #
# # for i in s:
# #     print(i, end=' ')
#
# # a = int(input())
# # a, b, c = 1, 1, 1
# # for i in range(a):
# #     summ = a + b + c
#
# # class Base:
# #     def __init__(self, chester, top):
# #         self.chester = chester
# #         self.top = top
# #
# #     def check(self):
# #         if self.chester == True and self.top == True:
# #             print('BASE 100%')
# #         else:
# #             print('NOT YET')
# #         return ''
# #
# #
# # masha = Base(True, True)
# #
# # print(masha.check())
#
#
#
# # class LittleBell():
# #     def __init__(self):
# #         pass
# #     def sound(self):
# #         print('ding')
# # bell = LittleBell()
# # # bell.sound()
#
# #
# # class Soda:
# #     def __init__(self, top):
# #         self.top = top
# #
# #     def show_my_drink(self):
# #         if self.top is not None:
# #             print('Газировка и', self.top)
# #         else:
# #             print('Обычная газировка')
# #
# # t = input()
# # if len(t) != 0:
# #     gaz = Soda(t)
# # else:
# #     gaz = Soda(None)
# # gaz.show_my_drink()
#
#
#
# class Nikola:
#     def __init__(self, n, age):
#         self.n = n
#         self.age = age
#         if 'Николай' != n:
#             print(f'Я не {n}, а Николай')
#         else:
#             pass
# p = Nikola('Max', 13)
# # print(p)


# class Sphere:
#
#     def __init__(self, r=1, x=0, y=0, z=0):
#         self.r = r
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def get_volume(self):
#         return 1 * ((3.14 * self.r ** 3) / 3)
#     def get_square(self):
#         return 4 * 3.14 * self.r ** 2
#     def get_radius(self):
#         return self.r
#     def get_center(self):
#         return self.x, self.y, self.z
#     def set_radius(self):
#         self.x, self.y, self.z = int(input().split())
#     def is_point_inside(self, x1, y1, z1):
#         return True if (self.x - x1) ** 2 + (self.y - y1) ** 2 + (self.z - z1) ** 2 <= self.r else False
#
# e = Sphere(3, 0, 0, 0)
# print(e.is_point_inside(9, 9, 9))

# my_tuple = []
# t = []
# s = input()
# a = list(map(int, input().split()))
# b = tuple(list(map(int, input().split())))
# c = tuple(list(map(int, input().split())))
# n = int(input())
# k = int(input())
#
# my_tuple.append(s)
# my_tuple.append(a)
# t.append(b)
# t.append(c)
# my_tuple.append(tuple(t))
#
# my_tuple = tuple(my_tuple)
# print(my_tuple)
# print(my_tuple[n][k])


# my_tuple_1 = []
# my_tuple_2 = []
#
# a = input()
# c = input()
# b = tuple(map(int, input().split()))
# d = tuple(map(int, input().split()))
# my_tuple_1.append(a)
# my_tuple_1.append(b)
# my_tuple_2.append(c)
# my_tuple_2.append(d)
#
# my_tuple_1 = tuple(my_tuple_1)
# my_tuple_2 = tuple(my_tuple_2)
#
# if my_tuple_1 > my_tuple_2:
#     print(my_tuple_1[0])
# else:
#     print(my_tuple_2[-1])
# my_tuple= (0, 1, 2, 3, 4, 5, 6)
# print(my_tuple[2])
# print(my_tuple[-2])
# print(my_tuple[:3])
#
#
# for i in range(len(my_tuple)):
#     if i == len(my_tuple):
#         print(my_tuple[i], '\n')
#         break
#
#     if i % 2 == 0:
#         print(my_tuple[i], end=' ')
#
# # print('\n')
#
# for i in range(len(my_tuple)):
#     if i == len(my_tuple):
#         print(my_tuple[i], '\n')
#         break
#
#     if i % 2 != 0:
#         print(my_tuple[i], end=' ')
#
# # print('\n')
# print(my_tuple[::-1])


a = [50, 41, 45, 12, 74, 56]
b = [13, 78, 50, 50, 46, 70, 90]
c = []
t = []

for i in a:
    t.append(i)
    t.append(1)
    c.append(t)
    t = []

for i in b:
    t.append(i)
    t.append(2)
    c.append(t)
    t = []

c = sorted(c)

count = 1
for i in c:
    i.append(count)
    count += 1

temp = []

for i in range(len(c) - 1):
    if c[i][0] == c[i + 1][0]:
        temp.append(c[i][-1])

    if c[i][0] != c[i + 1][0] and c[i][0] == c[i - 1][0]:
        temp.append(c[i][-1])

S = int(sum(temp) / len(temp))


for i in range(len(c) - 1):
    if c[i][0] == c[i + 1][0]:
        c[i][-1] = S

    if c[i][0] != c[i + 1][0] and c[i][0] == c[i - 1][0]:
        c[i][-1] = S


R = 0

if len(b) < len(a):
    for i in c:
        if i[1] == 2:
            R += i[-1]

else:
    for i in c:
        if i[1] == 1:
            R += i[-1]


print(R)
print(S)
print(temp)
print(c)

