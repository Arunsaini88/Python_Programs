from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizeinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="Score=0", fg="white", bg=THEME_COLOR)
        self.score_lable.grid(row=0, column=1)


        self.canves = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canves.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canves.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_check)
        self.true_button.grid(row=2, column=0, )

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_check)
        self.false_button.grid(row=2, column=1, )
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canves.config( bg="white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canves.itemconfig(self.question_text, text=q_text)
        else:
            self.canves.itemconfig(self.question_text, text="You1ve reach the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canves.config(bg="green")

        else:
            self.canves.config(bg="red")

        self.window.after(1000, self.get_next_question,)
        #self.canves.config( bg="white")