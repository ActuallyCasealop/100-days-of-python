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

coin_value = {
    'quarters':0.25,
    'dimes':0.10,
    'nickles':0.05,
    'pennies':0.01
}

def check_resources(drink):
    for key, value in MENU[drink]['ingredients'].items():
        if resources[key] < value:
            print(f"Insufficient {key}; Please contact the vendor for refill.")
            return False
    return True

def create_drink(drink):
    global resources

    for key, value in MENU[drink]['ingredients'].items():
        resources[key] -= value
    print(f"Enjoy your {drink}")

def check_coins(drink):
    global user_coins
    global total_coins

    if MENU[drink]['cost'] <= user_coins:
        total_coins += MENU[drink]['cost']
        user_coins -= MENU[drink]['cost']
        return True
    return False

total_coins = 0

while True:
    user_input = input(">>>: ")
    if user_input not in ['espresso','latte','cappuccino','off','report']:
        print("Invalid entry; please try again")
    else:
        if user_input == 'off':
            break
        elif user_input == 'report':
            for key, value in resources.items():
                print(f"{key} : {value}")
            print(f"Money : {total_coins}")
        else:
            user_coins = 0
            if check_resources(user_input) == True:
                    for coin in coin_value:
                        coin_input = int(input(f"How many {coin}?\n>>>: "))
                        user_coins += coin_input*coin_value[coin]
                    
                    if check_coins(user_input) == True:
                        create_drink(user_input)
                        print(f"here is your change: {"{:0.2f}".format(user_coins)}")
                    else:
                        print("Insufficient Fund; refunding.")
            else:
                break       