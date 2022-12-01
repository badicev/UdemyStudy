import turtle
# binbin = turtle.Turtle()

# or

from turtle import Turtle, Screen

binbin = Turtle()
print(binbin)
binbin.shape("turtle")
binbin.color("DarkOliveGreen4")

colors = ["cyan", "green", "red", "orange", "blue"]

binbin.speed(0)
for x in range(200):
    binbin.pencolor(colors[x % 5])
    binbin.width(x / 100 + 5)
    binbin.forward(x)
    binbin.left(59)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.bgcolor("black")
my_screen.exitonclick()
