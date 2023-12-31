from random import *

from art import logo

def deal_card():
    ''' Return a random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = choice(cards)
    return card

def calculate_score(cards):
    ''' Take a list of cards and return the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw "
    
    elif user_score == 0:
        return "Win with a Blavkjack"
    
    elif user_score > 21:
        return "You went over. You lose"

    elif computer_score >21:
        return "Opponent went over.You win"

    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose" 

def play_game():

    print(logo)  
    uesr_card = []
    computer_card = []

    for _ in range(2):
        uesr_card.append(deal_card())
        computer_card.append(deal_card())

    while True:

        user_score = calculate_score(uesr_card)
        computer_score = calculate_score(computer_card)
        print(f"Your card : {uesr_card}, current score {user_score}")
        print(f"computer first card: {computer_card[0]} ")

        if user_score == 0 or computer_score == 0 or user_score >21:
            break
        else:
            user_should_deal = input("Type 'y' to get another card. type 'n' to pass :")
            if user_should_deal == 'y':
                uesr_card.append(deal_card())
            else:
                break

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"  Youe final hand: {uesr_card}, final score: {user_score}")
    print(f"  Computer`s final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you went to play a game of Blackjack? Type 'y' or 'n' ") == 'y':
    play_game()
