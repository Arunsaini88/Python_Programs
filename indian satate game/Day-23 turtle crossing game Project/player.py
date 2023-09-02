from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.start_position()


    def game_over(self):
        self.write(f"Game Over", align="center", font=("Councilmen", 60, "normal"))
    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_position(self):
        self.goto(STARTING_POSITION)

    def go_to_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

