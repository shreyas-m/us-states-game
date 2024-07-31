import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
print(states)

states_identified = []

while len(states_identified) < 50:
    answer = screen.textinput(f"{len(states_identified)}/50 Guess the State Name", "Enter state name:").title()
    if answer in states:
        states_identified.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(data[data.state == answer].x.item(), data[data.state == answer].y.item())
        t.write(answer)
    elif answer == "Exit":
        break

remaining = []
for st in states:
    if st not in states_identified:
        remaining.append(st)
print(len(remaining))
pandas.DataFrame(remaining).to_csv("remaining.csv")
