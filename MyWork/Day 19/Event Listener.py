from turtle import Turtle, Screen

bin = Turtle()
screen = Screen()


# W: Forwards
# S: Backwards
# A: Counter-Clockwise
# D: Clockwise
# C: Clear drawing


def move_forwards():
    bin.forward(10)


def move_backwards():
    bin.backward(10)


def turn_left():
    new_heading = bin.heading() + 10
    bin.setheading(new_heading)


def turn_right():
    new_heading = bin.heading() - 10
    bin.setheading(new_heading)


def clear():
    bin.clear()
    bin.penup()
    bin.home()
    bin.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
