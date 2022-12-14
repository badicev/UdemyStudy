# open file with russian alphabet
import codecs
import sys
from tkinter import *

# with codecs.open('Ru-Alphabet.csv', 'r', encoding='utf-8') as f:
#     data = f.read()
#     print(data)

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

window.config(padx=50, pady=50, bg=LIGHT_GREEN)

canvas = Canvas(width=800, height=526, bg=LIGHT_GREEN, highlightthickness=False)
canvas.grid(column=1, row=0)

# IMAGE-PATH

import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


front = PhotoImage(file=resource_path("images/card_front.png"))
back = PhotoImage(file=resource_path("images/card_back.png"))
right = PhotoImage(file=resource_path("images/right.png"))
wrong = PhotoImage(file=resource_path("images/wrong.png"))
button = Button(image=front, highlightthickness=0)
canvas.grid(column=1, row=2, columnspan=2)
canvas.create_image(350, 213, image=front)




window.mainloop()