from turtle import Turtle

STATES_NUMBER = 50

FONT = ("Courier", 54, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 280)
        self.score = 0

    def write_new_score(self):
        argument = f"{self.score}/{STATES_NUMBER}"
        self.write(argument, False, "center", FONT)

    def change_score(self):
        self.clear()
        self.score += 1
        self.write_new_score()

    def complete_quiz_check(self):
        if self.score == STATES_NUMBER:
            self.clear()
            self.write("Well done! You got all the states right.", False, "center", ("Courier", 24, "normal"))
            return True

