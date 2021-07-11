import turtle
import pandas as pd
from player import Player

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
print(state_list)

chase = Player()

guess_states = []
while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 State Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guess_states.append(answer_state)
        x_cor = int(data.x[data.state == f"{answer_state}"])
        y_cor = int(data.y[data.state == f"{answer_state}"])
        chase.correct_answer(answer=answer_state, x=x_cor, y=y_cor)



screen.exitonclick()
