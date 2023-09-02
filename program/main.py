from art import logo

print(logo)
bids = {}

# Deffine a function to chosing higest Amount of bid . 
def find_higest_bidder(bidder_record):
    higest_amount = 0
    winner = ''
    # Loop for get Key(bidder) and value.
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        # Check the Largest amount .
        if bid_amount > higest_amount:
            higest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of {higest_amount}")



while True:
    name = input("What is your name ? :")
    price = int(input("What is your bid? : $"))
    # To ADD the item in the  Empty Dictionary.

    bids[name] = price
    Option = input("Aru there any other bidder? Tyoe 'yes' or 'no' ")
    if Option == 'no':
       # Calling the function 

        find_higest_bidder(bids)
        break