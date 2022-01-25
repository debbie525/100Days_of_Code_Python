# Virtual Coffee Machine
# - accepts order of 3 coffee types (latte, espresso and cappuccino)
# - can check available resources (water, milk and coffee)
# - can generate a report of available resources and profit
# - accepts 4 types of coins (quarter, dime, nickle and penny)
# - the virtual coffee machine can be turned-off for maintenance.

from art import logo

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(water, milk, coffee, money):
    print(f"Water : {water}ml")
    print(f"Milk : {milk} ml")
    print(f"Coffee: {coffee} ml")
    print(f"Money: ${money}")


def check_resource_espresso(water, coffee, MENU):
    """ if remaining water is less than zero, resource is insufficient"""
    remaining_water = water - MENU["espresso"]["ingredients"]["water"]
    remaining_coffee = coffee - MENU["espresso"]["ingredients"]["coffee"]
    if remaining_water < 0:
        print("Sorry, there is not enough water.")
        return 0
    elif remaining_coffee < 0:
        print("Sorry , there is not enough coffee")
        return 0
    else:
        return 1


def check_resource_latte(water, milk, coffee, MENU):
    """ if remaining water is less than zero, resource is insufficient"""
    remaining_water = water - MENU["latte"]["ingredients"]["water"]
    remaining_milk = milk - MENU["latte"]["ingredients"]["milk"]
    remaining_coffee = coffee - MENU["latte"]["ingredients"]["coffee"]
    if remaining_water < 0:
        print("Sorry, there is not enough water.")
        return 0
    elif remaining_milk < 0:
        print("Sorry, there is not enough milk.")
        return 0
    elif remaining_coffee < 0:
        print("Sorry , there is not enough coffee")
        return 0
    else:
        return 1


def check_resource_cappuccino(water, milk, coffee, MENU):
    """ if remaining water is less than zero, resource is insufficient"""

    remaining_water = water - MENU["cappuccino"]["ingredients"]["water"]
    remaining_milk = milk - MENU["cappuccino"]["ingredients"]["milk"]
    remaining_coffee = coffee - MENU["cappuccino"]["ingredients"]["coffee"]

    if remaining_water < 0:
        print("Sorry, there is not enough water.")
        return 0
    elif remaining_milk < 0:
        print("Sorry, there is not enough milk.")
        return 0
    elif remaining_coffee < 0:
        print("Sorry , there is not enough coffee")
        return 0
    else:
        return 1


def order(user_input):
    if user_input == "off":
        print("Coffee machine is off...")
        resume = 0
    elif user_input == "report":
        report(water, milk, coffee, money)
        resume = 0
    elif user_input == "espresso":
        resume = check_resource_espresso(water, coffee, MENU)
    elif user_input == "latte":
        resume = check_resource_latte(water, milk, coffee, MENU)
    elif user_input == "cappuccino":
        resume = check_resource_cappuccino(water, milk, coffee, MENU)
    else:
        print("Invalid response")
        resume = 0
    return resume

# ---------------------------------------------------------------------------------

print(logo)

user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

machine_off = False

while machine_off is False:
    if order(user_input) == 1:   # the user ordered coffee and the resources are available
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        total_coins = (0.25*quarters) + (0.1*dimes) + (0.05*nickles) + (0.01*pennies)
        cost = MENU[user_input]["cost"]

        print(f"Total coins inserted: ${total_coins}")
        print(f"Total Cost of {user_input}: ${cost}")

        if total_coins == cost:            # user inserted enough amount
            print("Exact amount received.")
            transaction_successful = "yes"
        elif total_coins > cost:           # user inserted too much money
            change = total_coins - cost    # calculate change of user
            print(f"Here is ${round(change,2)} in change.")    # round off to 2 decimal places
            transaction_successful = "yes"
        else:
            print("Sorry that's not enough money. Money refunded.")
            transaction_successful = "no"

        if transaction_successful == "yes":
            money += cost                # add as profit
            if user_input == "espresso":
                water -= MENU[user_input]["ingredients"]["water"]
                coffee -= MENU[user_input]["ingredients"]["coffee"]

            elif user_input == "latte" or user_input == "cappuccino":
                water -= MENU[user_input]["ingredients"]["water"]
                coffee -= MENU[user_input]["ingredients"]["coffee"]
                milk -= MENU[user_input]["ingredients"]["milk"]

            print(f"Here is your {user_input}. Enjoy!")

    elif user_input == "off":
        machine_off = True
        print("Machine is off.")
        break

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        machine_off = True
        print("Machine is off.")

