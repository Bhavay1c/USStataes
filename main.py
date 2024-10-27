#  this game basically asks you to guess the name of the stats of the us
# you have to guess all 50 states and at the end it displays the results and when user eneters exit it quits the operation and show unguessed state on console and also save in unguessed.csv 

import turtle
import pandas

screen = turtle.Screen()
screen.title("US state guesser")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

stateData = pandas.read_csv("50_states.csv")
guessedState = []

while len(guessedState)<50:
    answer_state = screen.textinput(f"{len(guessedState)}/50 guessed.", "Enter the state name").title()

    if answer_state == "Exit":

        break
    for index, s in enumerate(stateData["state"]):
        if answer_state == s:
            guessedState.append(s)
            t = turtle.Turtle()
            t.hideturtle()
            x = stateData["x"][index]
            y = stateData["y"][index]

            # Move the turtle to a specific location
            t.penup()

            t.goto(x, y)  # Replace with your desired coordinates

            # Write text at the current turtle position
            t.write(answer_state)

un_guessedState =[]
for state in stateData["state"]:
    if state not in guessedState:
        un_guessedState.append(state)


print(un_guessedState)
dframe = pandas.DataFrame(un_guessedState)
dframe.to_csv("unguessed.csv")
screen.exitonclick()

