import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("Game")
image = "Ankara.gif"
turtle.addshape(image)

turtle.shape(image)

#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
guessed_districts = []

while len(guessed_districts) < 25:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/50 ilçe doğru.",
                                       prompt="Bir ilçe adı söyleyiniz.").title()

    districts = pd.read_csv("districts.csv")
    all_districts = districts.district.to_list()

    if answer_district == "Exit":
        missing_districts = []
        for district in all_districts:
            if district not in guessed_districts:
                missing_districts.append(district)
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("districts_that_you_should_learn")
        break

    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = districts[districts.district == answer_district]
        t.goto(int(district_data.x), int(district_data.y))
        t.write(district_data.district.item())
