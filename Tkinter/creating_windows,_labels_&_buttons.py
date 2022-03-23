import tkinter
from tkinter import Button

windows = tkinter.Tk()              # window created

""" if we run this code till above we will get no screen hence we need a way of keeping the window on screen; so to do 
that we need to add 'windows.mainloop()' at the end of the code to keep our window sceen"""

windows.title("My First GUI Program")
windows.minsize(width=500, height=300)


""" ----------- Creating Labels ----------- """
my_label = tkinter.Label(text="Hello! I'm the label", font=("Arial",24,"italic"))         # creating a label is not enough to place it on the window
my_label.pack()                                             # the pack method will put the label at middle of the window
# my_label.pack(side="left")                                # this method will put the label at left of the window
# my_label.pack(expand=True)                                  # this method will put the label at center of the window



""" changing text of the label """

# my_label['text'] = "New Text"
# # or
# my_label.config(text="New Text")


""" Refer docs for packer :
            https://www.tutorialspoint.com/python/tk_pack.htm
            https://docs.python.org/3/library/tkinter.html
"""




def change_text_of_label():
    my_label['text'] = "I got clicked"




""" ----------- Creating Buttons ----------- """

button = Button(text="Click Me", command=change_text_of_label)            # the 'command' is used to perform action we want; we define our function name in command
button.pack()                                   # placing button on screen







windows.mainloop()              # helps in screen interaction