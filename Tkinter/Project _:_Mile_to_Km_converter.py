import tkinter
from tkinter import Button, Entry

# window
windows = tkinter.Tk()              # window created
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)
windows.config(padx=20, pady=20)            # padding

# text entry
input = Entry(width=20)
input.grid(column=1, row=0)


# miles
mile_label = tkinter.Label(text="Miles", font=("Arial",20,"italic"))
mile_label.grid(column=2, row=0)


# is equal to
eq_label = tkinter.Label(text="is equal to", font=("Arial",20,"italic"))
eq_label.grid(column=0, row=1)

# km result label
km_result_label = tkinter.Label(text="0", font=("Arial",20,"italic"))
km_result_label.grid(column=1, row=1)

# km
km_label = tkinter.Label(text="Km", font=("Arial",20,"italic"))
km_label.grid(column=2, row=1)



# calculate button
def calc():
    m = float(input.get())
    km_val = round(m*1.609)
    km_result_label.config(text=f"{km_val}")


calculate = Button(text="Calculate", command=calc)
calculate.grid(column=1, row=2)


windows.mainloop()