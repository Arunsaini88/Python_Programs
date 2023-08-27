print('Welcome to Treasure Island')
print('Your mission is to find the trreasure')
option1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n" ).lower()
if option1 == 'left':
    option2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to want for a boat. Typoe "swim" to swim across.\n').lower()
    if option2 == 'wait':
        option3 = input('You arrive at the island unharmed. There is a house with 3 doore .One red one is blue and one is yellow. Which colour do you chose? \n').lower()
        if option3 == 'yellow':
            print('You found the treasure! You are win')
        elif option3 == 'red':
            print('you enter the beast room.Game Over')
        elif option3 == 'blue':
            print('you enter the devil room.Game over')
        else:
            print('You chose the door does not exist.Game over')
    else:
        print('You got attacked by an angry trout.Game Over')
else:
    print('You fell into a hole.Game Over')
