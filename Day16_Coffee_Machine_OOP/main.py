from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_on = False
        print("Machine is Off.")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        order = menu.find_drink(choice)
        cost = order.cost
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(order)
    else:
        print("Invalid input.")

