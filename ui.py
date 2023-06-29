from tkinter import *
from PIL import Image, ImageTk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_STYLE = ("helvetica", 14, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x500")
        self.window.configure(bg=THEME_COLOR)

        # scoreboard ->
        self.currscore = Label(
            self.window, text=f"Score : {self.score}", font=FONT_STYLE, bg=THEME_COLOR, fg="white")
        self.currscore.place(x=125, y=10)

        # displaying question ->
        question = self.quiz_brain.next_question()
        self.label = Label(self.window, text=question,
                           font=FONT_STYLE, width=25, height=12, fg=THEME_COLOR, wraplength=230)
        self.label.place(x=35.5, y=75)

        # buttons ->
        img = Image.open("images/true.png")
        self.correct_button_img = ImageTk.PhotoImage(img)
        self.correct_button = Button(
            self.window, image=self.correct_button_img, command=self.answer_true)

        self.correct_button.place(x=50, y=375)

        self.user_answer = False
        img = Image.open("images/false.png")
        self.wrong_button_img = ImageTk.PhotoImage(img)
        self.wrong_button = Button(
            self.window, image=self.wrong_button_img, command=self.answer_false)

        self.wrong_button.place(x=200, y=375)

        self.window.mainloop()

    def scoreboard(self):
        self.score += 1
        self.currscore.config(text=f"Score : {self.score}")

    def next_Question(self):
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.label.config(text=question)
        else:
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.label.config(text=f"Final Score : {self.score}")
            self.currscore.config(text="")

    def answer_true(self) -> str:
        user_answer = str(True)
        result = self.quiz_brain.check_answer(user_answer=user_answer)
        if result:
            self.scoreboard()
        self.next_Question()

    def answer_false(self) -> str:
        user_answer = str(False)
        result = self.quiz_brain.check_answer(user_answer=user_answer)
        if result:
            self.scoreboard()
        self.next_Question()
