from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_input = input(f"What would you like?\n{menu.get_items()}\n>>>: ")
    if user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_input == 'off':
        break
    else:
        user_input = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(user_input) and money_machine.make_payment(user_input.cost) == True:
            coffee_maker.make_coffee(user_input)
        else:
            break
        