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
reps = 0
window_timer = None

""" ---------------------------- TIMER RESET ------------------------------- """
def reset_timer():
    window.after_cancel(window_timer)                   # this will cancel the timer we set previously
    timer.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    chk_mark.config(text = "")
    global reps
    reps=0


""" ---------------------------- TIMER MECHANISM ------------------------------- """
def start_timer():
    global reps
    reps += 1
    print(reps)

    work_sec = WORK_MIN * 60                # converting into seconds
    short_break_sec = SHORT_BREAK_MIN * 60              # converting into seconds
    long_break_sec = LONG_BREAK_MIN * 60                # converting into seconds

    if reps == 8:
        count_down(long_break_sec)
        timer.config(text="Long-Break", fg=RED)
        return
    elif reps % 2 == 0 and reps < 8:
        count_down(short_break_sec)
        timer.config(text="Short-Break", fg=PINK)
    elif reps % 2 != 0  and reps < 8:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)





""" ---------------------------- COUNTDOWN MECHANISM ------------------------------- """

# # thinking of a solution for countdown, we might think of the below approach; but as we are working with GUI and
# # through 'window.mainloop()' it needs to keep watching the screen every second that something happened or not
# # (to see whether if a user have some event) and the moment screen notice some event it's got to react to that event
# # hence GUI programs are 'Event Driven' through 'window.mainloop()' and if we set another loop in our program like
# # below it won't be able to reach the mainloop and while running the program nothing happens.



# import time
# def start_countdown():
#     i=5
#     while i>=0:
#         canvas.itemconfig(timer_text, text=f"{i}")            # itemconfig() for canvas
#         time.sleep(1)
#         i-=1


# # so in order to have an interactive program tkinter provides "after" method, It execute a command after a time delay.
# # syntax : after(self, ms, function, *args)   ;   ms = millisecond

def count_down(n):
    global window_timer
    count_min = n // 60
    count_sec = n % 60

    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if n > 0:
        window_timer = window.after(1000,count_down, n-1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        chk_mark.config(text=marks)



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
timer_text = canvas.create_text(100,129, text="00:00",fill="white", font=(FONT_NAME,25,"bold"))
canvas.grid(row=1, column=1)


# timer label
timer = Label(text="Timer",fg = GREEN,bg=YELLOW,font=(FONT_NAME,50))      # for text color we use foreground 'fg'
timer.grid(row=0, column=1)

# start button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

# reset button
reset = Button(text="Reset",highlightthickness=0, command = reset_timer)
reset.grid(row=2, column=2)

# check marks

chk_mark = Label(bg=YELLOW, fg='#41ab5b', font=(FONT_NAME,18))
chk_mark.grid(row=3, column=1)





window.mainloop()
