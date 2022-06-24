from coffee_recipes import MENU, resources, coins

# ================== check resources ===============


def check_resources(choice):
    for key in MENU[choice]["ingredients"]:
        menu_requirements = MENU[choice]["ingredients"][key]
        machine_stock = resources[key]
        if int(machine_stock) < int(menu_requirements):
            print(f"Sorry there is not enough {key}.")
            return False
        else:
            return True
# ================== use resources ===============


def use_resources(choice):
    for key in MENU[choice]["ingredients"]:
        menu_requirements = MENU[choice]["ingredients"][key]
        machine_stock = resources[key]
        resources[key] = int(machine_stock) - int(menu_requirements)
        return resources[key]
# ================== check coins ===============


def check_coins():
    quarters = int(input("How many quarter: "))
    dimes = int(input("How many dime: "))
    nickles = int(input("How many nickle: "))
    pennies = int(input("How many pennie: "))

    total_quarters = quarters * float(coins["quarter"])
    total_dimes = dimes * float(coins["dime"])
    total_nickles = nickles * float(coins["nickle"])
    total_pennies = pennies * float(coins["pennie"])

    total_coin = total_quarters + total_dimes + total_nickles + total_pennies
    return total_coin


serving = True
money = 0

while serving:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        serving = False
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")
    else:
        if check_resources(choice):

            choise_cost = float(MENU[choice]["cost"])

            total_coin = check_coins()

            if total_coin < choise_cost:
                print("Sorry that's not enough money. Money refunded.")
            elif total_coin == choise_cost:
                money = money + choise_cost
                use_resources(choice)
                print(f"Here is your {choice}. Enjoy! ☕")
            else:
                money = money + choise_cost
                refund = total_coin - choise_cost
                print(f"Here is ${'%.2f' % refund} dollars in change.")
                use_resources(choice)
                print(f"Here is your {choice}. Enjoy! ☕")
