import random
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? (red, purple, orange, green, blue, pink, black)")
# print(user_bet)

# easy way
is_race_on =  False
colors = ["red", "purple", "orange", "green", "blue", "pink", "black"]
y_pos = [150, 100, 50, 0, -50, -100, -150]
all_turtles = []



for turtle_index in range(0, 7):
    new_tospaa = Turtle(shape="turtle")
    new_tospaa.color(colors[turtle_index])
    new_tospaa.penup()
    new_tospaa.goto(x=-200, y=y_pos[turtle_index])
    all_turtles.append(new_tospaa)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


# red_turtle = Turtle(shape="turtle")
# red_turtle.penup()
# red_turtle.color("red")
#
# purple_turtle = Turtle(shape="turtle")
# purple_turtle.penup()
# purple_turtle.color("purple")
#
# orange_turtle = Turtle(shape="turtle")
# orange_turtle.penup()
# orange_turtle.color("orange")
#
# green_turtle = Turtle(shape="turtle")
# green_turtle.penup()
# green_turtle.color("green")
#
# blue_turtle = Turtle(shape="turtle")
# blue_turtle.penup()
# blue_turtle.color("blue")
#
# pink_turtle = Turtle(shape="turtle")
# pink_turtle.penup()
# pink_turtle.color("pink")
#
# black_turtle = Turtle(shape="turtle")
# black_turtle.penup()
# black_turtle.color("black")
#
# red_turtle.goto(x=-200, y=150)
# purple_turtle.goto(x=-200, y=100)
# orange_turtle.goto(x=-200, y=50)
# green_turtle.goto(x=-200, y=0)
# blue_turtle.goto(x=-200, y=-50)
# pink_turtle.goto(x=-200, y=-100)
# black_turtle.goto(x=-200, y=-150)

screen.exitonclick()
