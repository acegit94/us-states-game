import turtle
import pandas
from typing import Optional, Tuple

#### Create screen and turtle object
screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "./blank_states_img.gif"
screen.addshape(IMAGE)
turtle.showturtle()
turtle.shape(IMAGE)


#### Create pandas dataframe
US_STATES = pandas.read_csv("./50_states.csv")


def get_state_details(answer: str) -> Optional[Tuple[str, int, int]]:
    """Return state name and coordinates if exists
    otherwise return none"""
    us_state = US_STATES[US_STATES.state == answer]
    if us_state.empty:
        return None

    name = us_state.iloc[0].state
    x = us_state.iloc[0].x
    y = us_state.iloc[0].y
    return name, x, y

def fill_map(name: str, x: int, y: int, state_turtle: turtle.Turtle):
    """Fill state name on map"""
    state_turtle.setpos(x, y)
    state_turtle.write(name)

def game_logic():
    """Game logic"""
    correct_guesses = 0
    guessed_states = []

    while correct_guesses <= 50:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state name").title()
        if get_state_details(answer_state) is None:
            continue

        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        name, x, y = get_state_details(answer_state)
        fill_map(name, x, y, state_turtle)
        guessed_states.append(name)
        correct_guesses += 1


game_logic()
screen.mainloop()
