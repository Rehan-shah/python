from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to my coffee machine")
maker = CoffeeMaker()
cashier = MoneyMachine()

def cal():
    temp_money = 0
    quarters = int(input("How many quarters will you insert: "))
    dimes = int(input("How many dimes will you insert: "))
    nickles = int(input("How many nickles will you insert: "))
    pennies = int(input("How many pennies will you insert: "))
    temp_money += quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return temp_money

def run():
    menu = Menu()
    choice = input(f"Please choose {menu.get_items()} :")
    if choice == "report":
        maker.report()
        cashier.report()
        run()
    elif choice == "stop":
        print("thanks for using")
    else :
        choice = menu.find_drink(choice)
        if not (choice == None):
            if maker.is_resource_sufficient(choice):
                if cashier.make_payment(choice.cost) :
                    maker.make_coffee(choice)
        run()

run()


