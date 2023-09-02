import random
from turtle import *
from random import *

Anni = Turtle()
colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r,g,b)
    return random_color


Anni.speed('fastest')
def draw_spiralgraph(size_of_graph):
    for _ in range(360 // size_of_graph):
        Anni.color(random_color())
        Anni.circle(100)
        Anni.setheading(Anni.heading() + size_of_graph)

draw_spiralgraph(5)
screen = Screen()
screen.exitonclick()
