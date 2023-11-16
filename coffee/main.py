from data import MENU

money = 0
ingredients = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def run():
    global money,ingredients
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'report':
        print(
            f"Water: {ingredients['water']}\nMilk: {ingredients['milk']}"
            f"\nCoffee: {ingredients['coffee']}\nMoney: {money}")
        run()
    elif choice == "stop":
        print("Thanks for using")
    else:
        temp_money = cal()
        if process_ing(choice) and process_coin(choice, temp_money):
            for key in MENU[choice]["ingredients"]:
                ingredients[key] -= MENU[choice]["ingredients"][key]
            run()
        elif not process_ing(choice):
            print("Not enough ingredient in coffe machine sorry, returned all your money")
            run()
        else:
            print("You do not have enough returned all")
            run()


def process_coin(coffe_type, temp_money):
    if MENU[coffe_type]["cost"] > temp_money:
        return False
    else:
        change = round(temp_money - MENU[coffe_type]["cost"], 2)
        print(f"here your ${change} change")
        print("thanks for order")
        return MENU[coffe_type]["cost"]


def cal():
    temp_money = 0
    quarters = int(input("How many quarters will you insert: "))
    dimes = int(input("How many dimes will you insert: "))
    nickles = int(input("How many nickles will you insert: "))
    pennies = int(input("How many pennies will you insert: "))
    temp_money += quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return temp_money


def process_ing(coffe_type):
    for key in MENU[coffe_type]["ingredients"]:
        if ingredients[key] <= MENU[coffe_type]["ingredients"][key]:
            return False
    return True


run()
