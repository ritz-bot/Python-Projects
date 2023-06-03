#coffee machine
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


# TODO: 1 Print report of all cofee resources
# TODO: 2 Print report all cofFee resources
def is_resource_sufficient(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if resources[item]<=order_ingredients[item]:
            print("Sorry not enough stuff!!")
            is_enough=False
    return is_enough
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print('Here is your drink!!!')

def is_transaction_succesfule(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change=money_recieved-drink_cost
        print(f'Enjoy your drink and here is your ${change}')
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def process_coins():
    print('Insert the number of coins!!')
    total = int(input('How many quaters'))*0.25
    total+= int(input('How many dimes'))*0.10
    total+=int(input('How many nickes'))*0.05
    total += int(input('How many penis'))*0.01
    return total


profit=0
is_on=True
while is_on:
    choice=input('What would you like to have? espresso/latte/cappucino :')
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if is_transaction_succesfule(payment,drink['cost']):
                make_coffee(choice, drink['ingredients'])
