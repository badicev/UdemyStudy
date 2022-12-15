# http://www.russianforeveryone.com/RufeA/Lessons/Introduction/Alphabet/Alphabet.htm
# open file with russian alphabet
import codecs
import sys
from tkinter import *
import time

import pandas
# with codecs.open('Ru-Alphabet.csv', 'r', encoding='utf-8') as f:
#     data = f.read()
#     print(data)
# ---------------------------CHANGE MECHANISM--------------------------------#
import pandas as pd
import random

ru_alphabet_dict = {}

try:
    ru = pd.read_csv("data/letters_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Ru-Alphabet.csv")
    ru_alphabet_dict = original_data.to_dict(orient="records")
else:
    ru_alphabet_dict = ru.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(ru_alphabet_dict)
    canvas.itemconfig(up, text="Russian", fill="black")
    canvas.itemconfig(down, text=current_card["Russian"], fill="black")
    canvas.itemconfig(canvas_background, image=front)
    flip_timer = window.after(3000, func=flip)


def flip():
    # To change the image:

    canvas.itemconfig(up, text=current_card["English"], fill="white")
    canvas.itemconfig(down, text=current_card["Example"], fill="white")
    canvas.itemconfig(canvas_background, image=back)


def is_known():
    ru_alphabet_dict.remove(current_card)

    data = pandas.DataFrame(ru_alphabet_dict)
    data.to_csv("data/letters_to_learn", index=False)

    next_card()


# ---------------------------UI SETUP--------------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
ORANGE = "#FED049"
LIGHT_GREEN = "#CFFDE1"
MED_GREEN = "#68B984"
DARK_GREEN = "#3D5656"
FONT_NAME = "Courier"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=MED_GREEN)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, bg=MED_GREEN, highlightthickness=False)

# IMAGE-PATH

import os

# def resource_path(relative_path):
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)


front = PhotoImage(file="images/card_front.png")
canvas_background = canvas.create_image(400, 263, image=front)
up = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
down = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

back = PhotoImage(file="images/card_back.png")

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
