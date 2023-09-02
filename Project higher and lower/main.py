from art import *
from game_data import *
from random import *

print(logo)

def format_data(account):
    '''Takes the account data and return the printable formate'''
    account_name = account['name']
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a{account_descr}, from {account_country}"
def check_answer(guess,a_follower,b_follower):
    '''Use if statement to check if user correct'''
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'
score = 0
account_b = choice(data)
while True:
    account_a = account_b
    account_b = choice(data)
    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("who has more follower? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
   
    if is_correct:
        score +=1
        print(f"Your right ! Current score: {score}")
    else:
        print(f"Sorry, that`s wrong. Final score: {score}")
        break