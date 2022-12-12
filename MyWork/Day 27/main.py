import tkinter

# from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label.pack()
my_label.place(x=0, y=0)

my_label["text"] = "New Text"
# or
my_label.config(text="New Text")


# Button

def button_clicked():
    print(("I got clicked!"))
    my_label.config(text="Button got clicked!")


button = tkinter.Button(text="Click Me!", command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=20)
print(input.get())
input.pack()

# pack: packs widgets next to each other
# place: places to precise positions
# grid:




'''#######################'''
window.mainloop()
