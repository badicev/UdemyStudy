import tkinter

# from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
# or
my_label.config(text="New Text")


# Button

def button_clicked():
    print(("I got clicked!"))
    my_label.config(text="Button got clicked!")


button = tkinter.Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()


new_button = tkinter.Button(text="I am New!", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=20)
print(input.get())
input.grid(column=3, row=2)
# input.pack()

# pack: packs widgets next to each other
# place: places to precise positions
# grid: creates a collection of horizontal and vertical lines creating
# a pattern against which we can line up our design elements


'''#######################'''
window.mainloop()
