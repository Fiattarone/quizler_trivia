from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, q_brain: QuizBrain):
        self.quiz = q_brain
        self.window = Tk()
        self.window.title("Quizler_Trivia!")
        self.window.config(width=50, height=50, bg=THEME_COLOR, pady=20, padx=20)


        # self.background_image = PhotoImage(file="background.png")
        # self.canvas.create_image(150, 287, image="background_image")

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=275, text="Question text goes here", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        # print("True presssed")
        # self.score += 1
        # self.score = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        # self.score.grid(row=0, column=1)
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        # print("False pressed")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

