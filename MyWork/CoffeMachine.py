menu = {
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

total= 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money = 0
is_on = True


def is_resource(order_resources):
    for item in order_resources:
        if order_resources[item]>resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is your ${change}.")
        global money
        money += drink_cost
        return True
    else:
        print(f"Payment: {payment}")
        print("Sorry, that's not enough money. Try again.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")







while is_on:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "off":
        is_on = False
    elif answer == "report":
        print(f"Water {resources['water']} ml")
        print(f"Milk {resources['milk']} ml")
        print(f"Coffee {resources['coffee']} g")
        print(f"Money ${money}")
    else:
        drink = menu[answer]
        if is_resource(drink["ingredients"]):
            payment = process_coins()
            if is_success(payment, drink["cost"]):
                make_coffee(answer, drink["ingredients"])