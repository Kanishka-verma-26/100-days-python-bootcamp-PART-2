from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):          # ensuring to get object of QuizBrain class only


        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "italic"))
        self.score_label.grid(row=0, column=1,)

        self.canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
        self.canvas_ques = self.canvas.create_text(150, 150, width=270,text="Some ques",fill=THEME_COLOR, font=("Arial", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        True_img = PhotoImage(file="images/true.png")
        self.true = Button(image=True_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(row=2, column=0, )

        False_img = PhotoImage(file="images/false.png")
        self.false = Button(image=False_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(row=2, column=1, )


        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_ques, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_ques, text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_ques)           # after checking the answer looking for another question



