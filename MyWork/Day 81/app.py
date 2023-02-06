from tkinter import *
from morse import string_to_morse, morse_to_string

window = Tk()

def submit_to_morse():
    text = entry.get()
    morse = string_to_morse(text)
    entry.delete(0, END)
    entry.insert(0, morse)

def submit_to_text():
    morse = entry.get()
    text = morse_to_string(morse)
    entry.delete(0, END)
    entry.insert(0, text)
        
    
    
    #to text
    text = morse_to_string(morse)
    
    
    



submit_text_to_morse = Button(window, text="text-to-morse", fg="white", bg="#111111", command=submit_to_morse)
submit_text_to_morse.pack(side=BOTTOM)

submit_morse_to_text = Button(window, text="morse-to-text", fg="white", bg="#111111", command=submit_to_text)
submit_morse_to_text.pack(side=BOTTOM)



entry = Entry()
entry.config(font=("Ink Free", 24, "bold"))
entry.config(fg='white', bg='#111111', selectbackground='#111111')
entry.insert(0, "Enter your text here")
#delete when clicked
entry.bind("<Button-1>", lambda event: entry.delete(0, END))    
#entry.config(state=DISABLED)
entry.config(width=30)
entry.pack()
window.mainloop()


