import turtle
import pandas

from writer import Writer

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True
right_guess = 0

writer = Writer()
guess_state = []
while game_is_on:
    answer = screen.textinput(title=f"Guess the state {right_guess}/50", prompt="Write one of state name")
    data = pandas.read_csv("50_states.csv")

    if answer == "exit":
        break

    state = data[data.state == answer.title()]
    if not state.empty:
        writer.write(state.to_dict())
        right_guess += 1
        guess_state.append(answer.title())


states_need_know = data[~data['state'].isin(guess_state)]

states_need_know.to_csv("state_need_know.csv")