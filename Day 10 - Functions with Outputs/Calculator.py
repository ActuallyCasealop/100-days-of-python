import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def addition (num_1,num_2):
    return num_1 + num_2

def subtraction (num_1,num_2):
    return num_1 - num_2

def multiplication (num_1,num_2):
    return num_1 * num_2

def division (num_1,num_2):
    return num_1 /  num_2

calculation = True

operations = {
    '+':addition,
    '-':subtraction,
    'x':multiplication,
    '%':division
}

first_value = 0
while calculation:
    print(log)
    if not first_value:
        first_value = int(input("Please enter the first value.\n>>>: "))

    chosen_operator = input("Please select your desired operator\n>>>: ")
    if chosen_operator not in operations:
        print("Chosen Operator does not exist; chose choose another one.")
        chosen_operation = input("Please select your desired operator\n>>>: ")

    chosen_operation = operations[chosen_operator]
    second_value = int(input("Please enter the second value.\n>>>: "))
    operation_result = int(chosen_operation(first_value,second_value))

    print(f"{first_value} {chosen_operator} {second_value} = {operation_result}")

    user_input = input("would you like to continue from the last value? [Y] [N]\n>>>: ")
    if user_input.lower() == 'y':
        first_value = operation_result
    else:
        os.system('cls')
        first_value = 0