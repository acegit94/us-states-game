import turtle
import pandas

#### Create screen and turtle object
screen = turtle.Screen()
screen.title("U.S. States Game")
turtle.showturtle()
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#### Create pandas dataframe
us_states = pandas.read_csv("./50_states.csv")


state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()



def get_state_details(answer: str):
    us_state = us_states[us_states.state == answer]
    if len(us_state) == 0:
        return None

    name = us_state.state.item()
    x = us_state.x.item()
    y = us_state.y.item()
    return name, x, y

def fill_map(name: str, x: int, y: int):
    state_turtle.setpos(x, y)
    state_turtle.write(name)

def game_logic():
    """Game logic work"""
    correct_guesses = 0
    while correct_guesses <= 50:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state name")
        if get_state_details(answer_state) is None:
            continue
        name, x, y = get_state_details(answer_state)
        fill_map(name, x, y)

        correct_guesses += 1


game_logic()
screen.mainloop()