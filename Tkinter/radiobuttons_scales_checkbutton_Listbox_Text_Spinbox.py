from tkinter import Tk, IntVar, Button, Label, Entry,END, Radiobutton, Checkbutton, Text, Scale, Spinbox, Listbox


""" creating a new window and configuration """
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

""" Labels """
my_label = Label(text="Hello! I'm the label", font=("Arial",24,"italic"))         # creating a label is not enough to place it on the window
my_label.config(text="This is new text")
my_label.pack()

""" Buttons """
def change_input_text():
    new_text = input.get()
    my_label.config(text=new_text)

""" Entry """
input = Entry(width=35)
input.insert(END, string="Some text to begin with.")            # represents the point immediately after the last character entered by the user.
input.pack()

""" button """
button = Button(text="Click Me", command=change_input_text)
button.pack()

""" Text """
text = Text(width=30, height = 5)
text.focus_set()                            # It focuses the widget and makes them active until the termination of the program.
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.9",END))                  # gets current value in textbox at line 1, index/character 9
text.pack()

""" Spinbox """

def spinbox_used():
    print(spinbox.get())            # gets the current value in spinbox

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

""" Scale """
"""called with current scale value"""

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


""" Checkbutton """

def chkbtn_used():
    print(chkstate.get())               # print 1 if On button checked, else 0


chkstate = IntVar()                 # variable to hold on to checked state, 0 is off, 1 is on.
chkbtn = Checkbutton(text="Is On?", variable=chkstate, command=chkbtn_used)
chkstate.get()
chkbtn.pack()


""" Radiobutton """
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobtn1 = Radiobutton(text="Option1", value=1, variable = radio_state, command=radio_used)
radiobtn2 = Radiobutton(text="Option2", value=2, variable = radio_state, command=radio_used)
radiobtn3 = Radiobutton(text="Option3", value=3, variable = radio_state, command=radio_used)

radiobtn1.pack()
radiobtn2.pack()
radiobtn3.pack()


""" Listbox """
def listbox_used(event):
    print(listbox.get(listbox.curselection()))              # gets current selection from listbox

listbox = Listbox(height=4)
fruits = ["Apple","Mango","Orange","Banana","Strawberry"]
for i in fruits:
    listbox.insert(fruits.index(i),i)

listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()
