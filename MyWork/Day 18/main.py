from turtle import Turtle, Screen

binbin_the_tospaa = Turtle()
binbin_the_tospaa.shape("turtle")
binbin_the_tospaa.color("Green")
binbin_the_tospaa.pencolor("cyan3")

# for i in range(4):
#     binbin_the_tospaa.forward(100)
#     binbin_the_tospaa.left(90)

# for i in range(50):
#     binbin_the_tospaa.pencolor("")
#     binbin_the_tospaa.forward(10)
#     binbin_the_tospaa.pencolor("cyan")
#     binbin_the_tospaa.forward(10)


import random


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    binbin_the_tospaa.pencolor(R, G, B)


# for n in range(3, 10):
#      change_color()
#      for j in range(n):
#             binbin_the_tospaa.right(360 / n)
#             binbin_the_tospaa.forward(100)

#random walk
# angles = (0, 90, 180, 270 )
# for i in range(500):
#     binbin_the_tospaa.speed(0)
#     binbin_the_tospaa.pensize(10)
#     change_color()
#     binbin_the_tospaa.right(random.choice(angles))
#     binbin_the_tospaa.forward(50)


#Spirograph
for i in range(int(360)):
    change_color()
    binbin_the_tospaa.speed(0)
    binbin_the_tospaa.right(i)
    binbin_the_tospaa.circle(100)

my_screen = Screen()
my_screen.exitonclick()
