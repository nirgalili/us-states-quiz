import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state = State()

df = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
answer_df = df[df.state == answer_state]
answer_x = int(answer_df["x"])
answer_y = int(answer_df["y"])

print(answer_df)
if not answer_df.empty:
    state.write_new_state(answer_x, answer_y, answer_state)

screen.exitonclick()