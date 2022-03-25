from tkinter import *
import random
import pandas
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data ={}

"""_______________ csv to dict _______________"""
# orient determines the type of key-value pairs can be customized with the parameters
# refer documentation for more understanding "https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
# print(data_dict)



"""_______________ Command Functions _______________"""

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image= card_back_img)




"""_______________ Remove the current card from cards list _______________"""
def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)     # now it wont add the index no
    next_card()


"""_______________ Window setup _______________"""

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


"""_______________ Canvas _______________"""

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400,140,text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263,text="", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)



"""_______________ Buttons _______________"""

# unknown button
unknown_img = PhotoImage(file="images/wrong.png")
unknown = Button(image=unknown_img,  highlightthickness=0, command=next_card)
unknown.grid(row=1, column=0,)

flip_timer = window.after(3000, func=flip_card)


# known button
known_img = PhotoImage(file="images/right.png")
known = Button(image=known_img, highlightthickness=0, command=is_known)
known.grid(row=1, column=1, )




next_card()

window.mainloop()