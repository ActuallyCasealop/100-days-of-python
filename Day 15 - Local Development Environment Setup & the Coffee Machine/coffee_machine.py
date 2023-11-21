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

turned_on = True

while turned_on:
    user_input = input(">>>: ")
    if user_input not in ['espresso','latte','cappuccino','off','report']:
        print("Invalid entry; please try again")
    else:
        if user_input == 'off':
            break
        elif user_input == 'report':
            for key, value in resources.items():
                print(f"{key} : {value}")
        else:
            if check_resources(user_input) == True:
                create_drink(user_input)
            else:
                break
        