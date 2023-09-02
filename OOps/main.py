# from turtle import *
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(234)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pockemon',['Picachu','Squirtle','Charmander'])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table,)