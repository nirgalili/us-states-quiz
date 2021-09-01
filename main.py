import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
answer_df =  df[df.state == answer_state]
if answer_df.empty:
    print(("yes"))
else:
    print("no")





screen.exitonclick()