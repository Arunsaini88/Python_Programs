from turtle import *
from random import *
anni = Turtle()
colormode(255)
anni.speed("fastest")
anni.penup()
anni.hideturtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
anni.setheading(225)
anni.forward(300)
anni.setheading(0)
num_of_dots = 100

for dot_count in range(1,num_of_dots+1):
    anni.dot(20,choice(color_list))
    anni.forward(50)

    if dot_count % 10 == 0:
        anni.setheading(90)
        anni.forward(50)
        anni.setheading(180)
        anni.forward(500)
        anni.setheading(0)

screen = Screen()
screen.exitonclick()