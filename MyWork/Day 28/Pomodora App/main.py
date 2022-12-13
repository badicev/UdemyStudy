import sys
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
ORANGE = "#FED049"
LIGHT_GREEN = "#CFFDE1"
MED_GREEN = "#68B984"
DARK_GREEN = "#3D5656"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


# Reset Button
def Reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    my_label.config(text='Timer')
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If it is the 8th rep:
        countdown(long_break_sec)
        my_label.config(text='Take a longer break', bg=LIGHT_GREEN, fg=GREEN, font=(FONT_NAME, 50, 'bold'))

    elif reps % 2 == 0:
        # If it is the 2nd/4th/6th rep:
        countdown(short_break_sec)
        my_label.config(text='Take a short break', bg=LIGHT_GREEN, fg=PINK, font=(FONT_NAME, 50, 'bold'))
    else:
        # If it is the 1st/3rd/5th/7th ep:
        countdown(work_sec)
        my_label.config(text='Work time!', bg=LIGHT_GREEN, fg=RED, font=(FONT_NAME, 50, 'bold'))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# import time
from math import floor


#
# while True:
#     time.sleep(1)
#     count -= 1


# Start Button
def countdown(count):
    "04:50 format"
    min_count = floor(count / 60)
    sec_count = count % 60

    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=LIGHT_GREEN)

canvas = Canvas(width=512, height=600, bg=LIGHT_GREEN, highlightthickness=False)

# IMAGEPATH
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


tomato_img = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(250, 216, image=tomato_img)

##########
timer_text = canvas.create_text(250, 550, text="00:00", fill=DARK_GREEN, font=(FONT_NAME, 60, 'bold'))
canvas.grid(column=1, row=1)

# Timer Text
my_label = Label(text='Timer', bg=LIGHT_GREEN, fg=DARK_GREEN, font=(FONT_NAME, 50, 'bold'))
my_label.grid(column=1, row=0)

# calls action() when pressed
button = Button(text='Start', command=start_timer, fg=MED_GREEN, bg=ORANGE, font=(FONT_NAME, 30, 'italic'))
button.grid(column=0, row=2)

# calls action() when pressed
button = Button(text='Reset', command=Reset, fg=MED_GREEN, bg=ORANGE, font=(FONT_NAME, 30, 'italic'))
button.grid(column=2, row=2)

check_mark = Label(bg=LIGHT_GREEN, font=(FONT_NAME, 25, 'bold'))
check_mark.grid(column=1, row=3)

window.mainloop()
while True:
    pass
