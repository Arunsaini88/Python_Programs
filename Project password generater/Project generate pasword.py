from random import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z',
           'A', 'B''C', 'D', 'E', 'F', 'G', 'H', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symboles = ['@', '#', '$', '%', '&', '*', '!', '(', ')', '+', '*']

print('Welcome to the PyPassword generator')
nr_letters = int(input('How many letters would you like in your password :\n'))
nr_symbole = int(input(f'How many symbole would you like? :\n'))
nr_number = int(input(f'How many number would you like? :\n'))

# generate the password

password_list = []

for cha in range(1, nr_letters + 1):
    password_list += choice(letters)

for cha in range(1, nr_number + 1):
    password_list += choice(numbers)

for cha in range(1, nr_symbole + 1):
    password_list += choice(symboles)

shuffle(password_list)

password = ''

for char in password_list:
    password += char
print(f"Your Password is :{password}")
