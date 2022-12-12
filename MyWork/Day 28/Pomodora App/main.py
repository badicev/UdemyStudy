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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=LIGHT_GREEN)

FG = MED_GREEN

canvas = Canvas(width=512, height=600, bg=LIGHT_GREEN, highlightthickness=False)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(250, 216, image=tomato_img)
canvas.create_text(250, 550, text="00:00", fill=DARK_GREEN, font=(FONT_NAME, 60, "bold"))
canvas.grid(column=1, row=1)

# Timer Text
my_label = Label(text="Timer", bg=LIGHT_GREEN, fg=DARK_GREEN, font=(FONT_NAME, 50, "bold"))
my_label.grid(column=1, row=0)


# Start Button
def Start():
    print("Start Countdown")


# calls action() when pressed
button = Button(text="Start", command=Start, fg=MED_GREEN, bg=ORANGE, font=(FONT_NAME, 30, "italic"))
button.grid(column=0, row=2)


# Start Button
def Reset():
    print("Reset Countdown")


# calls action() when pressed
button = Button(text="Reset", command=Reset, fg=MED_GREEN, bg=ORANGE, font=(FONT_NAME, 30, "italic"))
button.grid(column=2, row=2)

check_mark = Label(text="✅", bg=LIGHT_GREEN, font=(FONT_NAME, 25, "bold" ))
check_mark.grid(column=1, row=3)

window.mainloop()
