from tkinter import *

import random
from tkinter import messagebox

FONT_NAME = "Courier"

""" ---------------------------- PASSWORD GENERATOR ------------------------------- """

def generate_pass():
    pass_str = ""
    for i in range(10):
        n = random.randint(33,122)
        pass_str += chr(n)
    print(pass_str)
    pass_input.insert(END,pass_str)






""" ---------------------------- SAVE PASSWORD ------------------------------- 
        _____________ Confirmation Popup _____________ 
         
         Tk library provides a set of dialogs that can be used to display message boxes, and to select files and colors,
        In addition, tkinter provides some simple dialogs allowing you to ask the user for integers, floating point values,
        and strings. One of the most popular standard dialogs are 'message boxes' """

def save_entry():
    web = web_input.get()
    em = email_input.get()
    ps = pass_input.get()

    if len(web)==0 or len(em)==0 or len(ps)==0:
        messagebox.showerror(title="Invalid Entry", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.showinfo(title=web, message=f"These are the details entered: \nEmail: {em} \nPassword: {ps} \nIs it ok to save?")

        if is_ok:
            with open("data.csv", mode="a") as file:
                file.write(f"{web} | {em} | {ps}\n")

            # clearing out the inputs after saving the data
            web_input.delete(0,END)
            pass_input.delete(0,END)


    print(web, em, ps)


""" ---------------------------- UI SETUP ------------------------------- """

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

"""_________ Labels _________"""

# website label
web_label = Label(text="Website:", font=(FONT_NAME,10), bg="white", pady=7)
web_label.grid(row=1, column=0)


# Email label
email_label = Label(text="Email/Username:", font=(FONT_NAME,10), bg="white", pady=7)
email_label.grid(row=2, column=0)

# password label
pass_label = Label(text="Password:", font=(FONT_NAME,10), bg="white", pady=7)
pass_label.grid(row=3, column=0)


""" __________ Buttons __________"""

# generate password button
gen_pass = Button(text="Generate Password",width=15, highlightthickness=0, bg="white", command=generate_pass)
gen_pass.grid(row=3, column=2)

# add button
add = Button(text="Add",highlightthickness=0,width=33, bg="white", command=save_entry)
add.grid(row=4, column=1, columnspan=2)


"""_________ Entries _________"""

# website name input
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

# email input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END,"kanishka@hashstudioz.com")

# password input
pass_input = Entry(width=21)
pass_input.grid(column=1, row=3,)



window.mainloop()
