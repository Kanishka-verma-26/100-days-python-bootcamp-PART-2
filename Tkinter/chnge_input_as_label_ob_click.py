import tkinter
from tkinter import Button, Entry

# window
windows = tkinter.Tk()              # window created
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="Hello! I'm the label", font=("Arial",24,"italic"))         # creating a label is not enough to place it on the window
my_label.pack()

# text entry
input = Entry(width=20)
input.pack()


def change_input_text():
    new_text = input.get()
    my_label.config(text=new_text)

# button
button = Button(text="Click Me", command=change_input_text)
button.pack()



windows.mainloop()