import turtle
import pandas
from state import State
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state = State()
scoreboard = Scoreboard()
scoreboard.write_new_score()

df = pandas.read_csv("50_states.csv")

user_guesses_list = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    answer_df = df[df.state == answer_state]
    answer_x = int(answer_df["x"])
    answer_y = int(answer_df["y"])

    # print(answer_df)
    if not answer_df.empty and answer_state not in user_guesses_list:
        state.write_new_state(answer_x, answer_y, answer_state)
        scoreboard.change_score()
        user_guesses_list.append(answer_state)

    if scoreboard.complete_quiz_check():
        game_is_on = False

    # print(user_guesses_list)

screen.exitonclick()