from questionary import select


from questionary import Validator, ValidationError, prompt, question
import questionary
from time import sleep


class NameValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text),
            )


class NumValidator(Validator):
    def validate(self, number):
        #print(f'document.text = {document.text}')
        try:
            x = int(number.text)
        except:
            raise ValidationError(
                message="Please enter an positive integer",
                # cursor_position=len(number.text)
            )


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


def Deduct(drink, credit):
    if credit == False:
        #print("Not enough credits")
        return
    drink = MENU[drink]
    # Deducting ingredients
    for i in drink["ingredients"]:
        resources[i] = resources[i] - drink['ingredients'][i]
        if resources[i] < 0:
            return print(f"\nNot enought {i}, please refill the machine")

    credit = "{:.2f}".format(credit - drink['cost'])
    print(f"Here's your change: ${credit}")
    print("(*⌒―⌒*) Enjoy your drink (*⌒―⌒*)")


def Refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def AskMoney(drinkCost, cents=0, nickels=0, dimes=0, quarters=0):
    cents = int(questionary.text(
        "How many cents you're using? ", validate=NumValidator).ask())
    nickels = int(questionary.text(
        "How many nickels you're using? ", validate=NumValidator).ask())
    dimes = int(questionary.text(
        "How many dimes you're using? ", validate=NumValidator).ask())
    quarters = int(questionary.text(
        "How many quarters you're using? ", validate=NumValidator).ask())
    total = cents/100 + nickels / 20 + dimes / 10 + quarters / 4
    if drinkCost > total:
        print("Not enough money for this drink!")
        return False
    else:
        return total


def PrintReport(resources, money):
    print(f'Money acquired today: {money}')
    for i in resources:
        print(f'{i.capitalize()}: {resources[i]}ml')


print('''
    ( (
    ) )
  ........
  |      |]
  \      /
   `----'
      ''')

money = 0
while True:
    user_choice = select("What would you like?",
                         choices=[
                             "Espresso",
                             "Latte",
                             "Cappuccino",
                             "Report",
                             "Refill",
                             "Exit"
                         ]).ask().lower()
    if user_choice == "espresso":
        print(f"The Espresso costs ${MENU[user_choice]['cost']}")
        credit = AskMoney(MENU[user_choice]['cost'])
        Deduct(user_choice, credit)
        money += MENU[user_choice]['cost']
        pass
    elif user_choice == "latte":
        print(f"The Latte costs ${MENU[user_choice]['cost']}")
        credit = AskMoney(MENU[user_choice]['cost'])
        Deduct(user_choice, credit)
        money += MENU[user_choice]['cost']
        pass
    elif user_choice == "cappuccino":
        print(f"The Cappuccino costs ${MENU[user_choice]['cost']}")
        credit = AskMoney(MENU[user_choice]['cost'])
        Deduct(user_choice, credit)
        money += MENU[user_choice]['cost']
        pass
    elif user_choice == "report":
        PrintReport(resources, money)
        pass
    elif user_choice == "refill":
        print("Refilling the machine...")
        sleep(3)
        Refill()
        print("(＾▽＾) Machine refilled with success (＾▽＾)")
        pass
    else:
        print("Exiting the program...")
        break
