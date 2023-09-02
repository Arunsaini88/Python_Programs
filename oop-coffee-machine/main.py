from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machin = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:
    option = menu.get_items()
    choice = input(f'What would you like? ({option}):')
    if choice == 'off':
        break
    elif choice == 'report':
        coffee_maker.report()
        money_machin.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machin.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

