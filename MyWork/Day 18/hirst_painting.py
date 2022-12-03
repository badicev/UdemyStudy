# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
#
# print(colors)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
import turtle
import random

color_list = [(180, 66, 21), (186, 14, 3), (215, 152, 98), (79, 38, 16), (229, 209, 186), (235, 163, 5), (246, 204, 0), (199, 3, 8), (235, 203, 98), (215, 79, 56), (50, 113, 161), (24, 185, 167), (115, 176, 166), (163, 55, 70), (25, 170, 199), (101, 167, 184), (94, 66, 22), (59, 125, 103), (213, 58, 70), (66, 24, 29), (239, 172, 153), (73, 119, 196), (25, 52, 33), (202, 214, 199), (195, 126, 144), (19, 95, 66), (35, 47, 58), (55, 56, 109), (231, 207, 210), (27, 82, 92)]

turtle.colormode(255)
binbin = turtle.Turtle()
binbin.speed(0)
binbin.penup()
binbin.hideturtle()


binbin.setheading((225))
binbin.forward((500))
binbin.setheading(0)

number_of_dots = 80

for dot_count in range(1, number_of_dots + 1):
    binbin.dot(40, random.choice(color_list))
    binbin.forward(100)

    if dot_count % 8 == 0:
        binbin.setheading(90)
        binbin.forward(80)
        binbin.setheading(180)
        binbin.forward(800)
        binbin.setheading(0)



from turtle import Turtle, Screen

my_screen = Screen()
my_screen.exitonclick()


