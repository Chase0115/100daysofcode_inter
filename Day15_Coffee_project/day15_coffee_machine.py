from menu import MENU, resources


water_left = resources["water"]
milk_left = resources["milk"]
coffee_left = resources["coffee"]
resources["money"] = 0
money_left = resources["money"]
# TODO5 : Process coins.
def add_coins():
    print("please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

# TODO4 : Check resources sufficient?
def check_resources(choice, water_left, milk_left, coffee_left, keep_running, MENU):
    water_left -= int(MENU[choice]["ingredients"]["water"])
    milk_left -= int(MENU[choice]["ingredients"]["milk"])
    coffee_left -= int(MENU[choice]["ingredients"]["coffee"])
    if water_left < 0:
        print("Sorry there is not enough water")
    elif milk_left < 0:
        print("Sorry there is not enough milk")

    elif coffee_left < 0:
        print("Sorry there is not enough coffee")




# TODO3 : print report
def report(water, milk, coffee, money):
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

keep_running = True
# Todo1 : Prompt user by asking "What would you like?" (espresso/latte/cappuccino): "
while keep_running:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO2 : turn off the Coffee Machine by entering "off" to the prompt
    if user_choice == "off":
        keep_running = False
    elif user_choice == "report":
        report(water_left,milk_left,coffee_left,money_left)
    else:
        keep_running = check_resources(user_choice, water_left, milk_left, coffee_left, keep_running,MENU)
        customer_paid = add_coins()
        cost = MENU[user_choice]["cost"]
        # TODO6 : Check transaction successful?
        if cost > customer_paid:
            print("Sorry, that's not enough money. Money refunded.")

        else:
            # TODO7 : Make Coffee.
            water_left -= MENU[user_choice]["ingredients"]["water"]
            milk_left -= MENU[user_choice]["ingredients"]["milk"]
            coffee_left -= MENU[user_choice]["ingredients"]["coffee"]
            change = format(customer_paid - cost,'.2f')
            money_left += cost
            print(f"Here is ${change} in change")
            print(f"Here is your {user_choice} ☕ Enjoy!")















