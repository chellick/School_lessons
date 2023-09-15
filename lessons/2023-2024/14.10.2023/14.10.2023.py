from turtle import *
speed(10)

# forward(100)
# right(90)
# forward(130)
# right(90)
# forward(100)
# right(90)
# forward(130)
# right(30)
# forward(100)
# right(90+30)
# forward(100)
# right(30)
# up()
# forward(20)
# right(90)
# forward(10)
# down()
# forward(25)
# left(90)
# forward(25)
# left(90)
# forward(25)
# left(90)
# forward(25)
# right(90)
# up()
# forward(10)
# right(90)
# forward(110)
# down()
# right(90)
# forward(30)
# right(90)
# forward(50)
# left(90)
# forward(40)
# right(90)
# up()
# forward(35)
# down()
# forward(25)
# left(90)
# forward(25)
# left(90)
# forward(25)
# left(90)
# forward(25)
# right(90)
# up()
# forward(35)
# down()
# forward(50)
# done()

k = 1
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5)

goto(0, 0)
down()

# for i in range(8):
#     forward(60)
#     right(120)

# goto(0, 0)
# done()

# right(315)

# for i in range(7):
#     forward(16*k)
#     right(45)
#     forward(8*k)
#     right(135)
# done()

# for i in range(6):
#     forward(10*k)
#     right(60)

right(180)
forward(5*k)
right(90)
forward(50)
right(90)
forward(5)

for i in range(5):
    seth(90)
    circle(-5*k, 180)

done()
