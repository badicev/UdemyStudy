# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
import sys
from tkinter import *
from tkinter import messagebox

# messagebox is not a class, it is another module


# Password Generator Project
import random


# import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    #
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 18))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    # pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #     password += char


#
# def generate_password():
#     password_input.insert(END, string=f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_user = website_input.get()
    email_user = email_input.get()
    password_user = password_input.get()
    new_data = {
        website_user: {
            "email": email_user,
            "password": password_user
        }
    }

    if len(website_user) == 0 or len(password_user) == 0:
        messagebox.showinfo(title="Oops", message="You have left empty field/s.")
    else:
        try:
            with open("pws.json", "r") as f:
                # reading the old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("pws.json", "w") as f:
                # saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD -------------------------- #

def search():
    website = website_input.get()
    try:
        with open("pws.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="Ooops", message = "No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showwarning(title="Ooops", message=f" No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
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
window.title("Password Manager")

window.config(padx=50, pady=50, bg=LIGHT_GREEN)

canvas = Canvas(width=600, height=600, bg=LIGHT_GREEN, highlightthickness=False)
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


logo = PhotoImage(file=resource_path("logo.png"))
canvas.create_image(300, 300, image=logo)

'''Texts'''
website = Label(text='Website:', fg=MED_GREEN, bg=LIGHT_GREEN, font=(FONT_NAME, 20, 'italic'))
website.grid(column=0, row=1)

email_username = Label(text='Email/Username:', fg=MED_GREEN, bg=LIGHT_GREEN, font=(FONT_NAME, 20, 'italic'))
email_username.grid(column=0, row=2)

Password = Label(text='Password:', fg=MED_GREEN, bg=LIGHT_GREEN, font=(FONT_NAME, 20, 'italic'))
Password.grid(column=0, row=3)

'''Buttons'''

# calls action() when pressed
generate_button = Button(text="Generate Password", command=generate_password, width=30, borderwidth=5, bg=PINK)
generate_button.grid(column=2, row=3, columnspan=2)

# calls action() when pressed
search_button = Button(text="Search", command=search, width=30, borderwidth=5, bg=PINK)
search_button.grid(column=2, row=1, columnspan=2)

# calls action() when pressed
add_button = Button(text="Add", width=70, command=save, borderwidth=5, bg=PINK)
add_button.grid(column=1, row=4)

'''Text Inputs'''

# Website
website_input = Entry(width=70, bg=ORANGE)
website_input.grid(column=1, row=1)
website_input.focus()

# E-mail/Username
email_input = Entry(width=70, bg=ORANGE)
email_input.insert(END, string="cevikbasakdilara@gmail.com")
email_input.grid(column=1, row=2)

# Password
password_input = Entry(width=70, bg=ORANGE)
password_input.grid(column=1, row=3)

window.mainloop()
