""" ----------------- Tkinter Layout Managers : pack(), place(), and grid() ----------------- """


""" pack() : packs each of the widget next to each other in a vaguely logical format; 
        it will always start from the top and then pack every other widget just below the previous one 
         
         pack() organizes widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions.
         Each box is offset and relative to each other. """


""" place() : places widgets in a two dimensional grid using x and y absolute coordinates. 
        the downside of place is the fact that it is so specific and we have to work out in our head the coordinate and 
        where to put each widget (suppose placing 100's of widgets using place() method )"""


""" grid() : locates widgets in a two dimensional grid using row and column absolute coordinates. 
        it imagines that your entire program is a grid and you can divide it into any no of columns and rows you want to"""


""" note: we can not use pack() with grid()"""


import tkinter
from tkinter import Button, Entry

# window
windows = tkinter.Tk()              # window created
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)
windows.config(padx=20, pady=20)            # padding


# label
my_label = tkinter.Label(text="Hello!", font=("Arial",24,"italic"))         # creating a label is not enough to place it on the window
# my_label.pack(side='left')
my_label.grid(column=0, row=0)


# text entry
input = Entry(width=20)
input.grid(column=3, row=2)                           # places the entry at top left corner


def change_input_text():
    new_text = input.get()
    my_label.config(text=new_text)

# button
button = Button(text="Click Me", command=change_input_text)
button.grid(column=1, row=1)


# new button
def do_nothing():
    pass

new_button = Button(text="New Button", command=do_nothing)
new_button.grid(column=2, row=0)



windows.mainloop()