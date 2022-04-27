from replit import clear
from machine import MENU, resources

resources["money"] = 0


# TODO: 4. Check if the resources are sufficient?
# TODO: 4a. When the user chooses a drink, the program should check if there are enough resources to make that dink

def check_resources(order_ingredients):
    """Takes in the user's choice dictionary and returns if there is enough resources to make the coffee"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_payment():
    """Returns the total value of the coins inserted"""
    # TODO: 5. Process coins
    # TODO: 5a. Prompt the user to insert coins:
    print("Please insert coins.")
    # TODO: 5b. calculate the monetary value of coins inserted
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if the money is insufficient"""
    # TODO: 6. Check if the transaction was successful?
    # TODO: 6a.Check that the user has inserted enough money to purchase the selected drink
    if money_received >= drink_cost:
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


# TODO: 1. Prompt user
# TODO: 1b. The prompt should show every time action has completed
next_user = True

while next_user:
    clear()
    choice: str = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 1a.Check the users input
    # # TODO: 2. Turn off the machine by entering "off" to the prompt
    if choice == "off":
        next_user: bool = False
    # # TODO: 3.Print report
    elif choice == 'report':
        print(
            f"water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g"
            f"\nMoney: ${resources['money']}")
    else:
        cost = MENU[choice]["cost"]
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_payment()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
