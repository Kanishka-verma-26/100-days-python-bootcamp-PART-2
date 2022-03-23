from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

""" ---------------------------- TIMER RESET ------------------------------- """

""" ---------------------------- TIMER MECHANISM ------------------------------- """

""" ---------------------------- COUNTDOWN MECHANISM ------------------------------- """

""" ---------------------------- UI SETUP ------------------------------- """
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# displaying tomato image
# canvas allows you to layer things one on top of the other
# such as placing image on our program and placing timer on image

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)              # same as tomato size; highlightthickness removes the unwanted border of the image
tomato_img = PhotoImage(file="tomato.png")           # Photoimage is one of the built-in methods which has been used to add the user-defined images in the application.
canvas.create_image(100, 112, image=tomato_img)         # placing image at half of the canvas coordinates
canvas.create_text(100,129, text="00:00",fill="white", font=(FONT_NAME,25,"bold"))
canvas.grid(row=1, column=1)


# timer label
timer = Label(text="Timer",fg = GREEN,bg=YELLOW,font=(FONT_NAME,50))      # for text color we use foreground 'fg'
timer.grid(row=0, column=1)

# start button
start = Button(text="Start", highlightthickness=0)
start.grid(row=2, column=0)

# reset button
reset = Button(text="Reset",highlightthickness=0)
reset.grid(row=2, column=2)

# check marks

chk_mark = Label(text=" ✅ ",bg=YELLOW)

chk_mark.grid(row=3, column=1)





window.mainloop()
