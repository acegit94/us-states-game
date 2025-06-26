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

    us_state = US_STATES[US_STATES.state == answer.title()]
    if us_state.empty:
        return None
    name = us_state.iloc[0].state
    x = us_state.iloc[0].x
    y = us_state.iloc[0].y
    return name, x, y

def fill_map(name: str, x: int, y: int):
    """Fill state name on map"""
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.setpos(x, y)
    state_turtle.write(name)

def missed_states_csv(all_states: list, guessed_states: list):
    """Create csv with missing states after game over"""
    missing_states = []
    missing_states = [state for state in all_states if state not in guessed_states]

    if missing_states:
        missed_data = pandas.DataFrame(missing_states)
        missed_data.to_csv("./missed.csv", index=False)

def game_logic():
    """Game logic"""
    correct_guesses = 0
    all_states = US_STATES.state.to_list()
    guessed_states = []

    while correct_guesses <= 50:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state name")
        if answer_state == "Exit" or answer_state is None:
            break
        if get_state_details(answer_state) is None:
            continue

        name, x, y = get_state_details(answer_state)
        if name not in guessed_states:
            fill_map(name, x, y)
            correct_guesses += 1
            guessed_states.append(name)

    missed_states_csv(all_states, guessed_states)

game_logic()
screen.mainloop()
