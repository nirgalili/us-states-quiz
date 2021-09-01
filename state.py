from turtle import Turtle

FONT = ("Courier", 8, "normal")


class State(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write_new_state(self, x, y, state_name):
        self.goto(x, y)
        self.write(state_name, False, "center", FONT)
