import turtle
import pandas

screen = turtle.Screen()
screen.title('Indian State Game')
image = 'blank_indian_img.gif'
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("indian state name.csv")
all_state = data['state'].tolist()
guessed_state = []

while len(guessed_state) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/29 Current State",
                                    prompt="What is another state name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        missing_state = [states for states in all_state if states not in guessed_state]
        # missing_state = []
        # for staste in all_state:
        #     if staste not in guessed_state:
        #         missing_state.append(staste)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn")
        print(missing_state)
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


screen.exitonclick()