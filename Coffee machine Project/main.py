MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficent(order_ingrsdient):
    """Returns True when order can be made, False if ingredient are insufficent."""
    for item in order_ingrsdient:
        if order_ingrsdient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def is_transection_successful(money_recived,drink_cost):
    """Return True when the payment is accepted, os False if money is insufficent."""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost,2)
        print(f"Here is ${change} is change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that`s not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredient from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.Enjoy!")

def process_coins():
    """Retuens the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?:"))* 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transection_successful(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])
