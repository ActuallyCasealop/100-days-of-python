import random, os
from data import data
from art import *

game_on = True
user_score = 0

def check_answer(response, first_data, second_data):
    global user_score, data, A_chosen_data

    if response == 'a':
        if first_data['follower_count'] > second_data['follower_count']:
            user_score += 1
            data.remove(second_data)
            return True
        else:
            return False
    elif response == 'b':
        if second_data['follower_count'] > first_data['follower_count']:
            user_score += 1
            A_chosen_data = second_data
            if first_data in data:
                data.remove(first_data)
            return True
        else:
            return False

A_chosen_data = random.choice(data)
data.remove(A_chosen_data)
print(logo)
while game_on:
    B_chosen_data = random.choice(data)
    print(f"{A_chosen_data['name']}, a {A_chosen_data['description']} from {A_chosen_data['country']}")
    print(vs)
    print(f"{B_chosen_data ['name']}, a {B_chosen_data ['description']} from {B_chosen_data ['country']}\n")
    print("which have has a higher follower count? [A] or [B]?")

    user_input = input(">>>: ").lower()
    while user_input not in ['a','b']:
        print("Invalid answer; Please try again.")
        user_input = input(">>>: ").lower()
    else:
        if check_answer(user_input, A_chosen_data, B_chosen_data) == True:
            os.system('clear')
            print(logo,f"\ncurrent score: {user_score}")
        elif check_answer(user_input, A_chosen_data, B_chosen_data) == False:
            print(f"Incorrect; you lose. final score: {user_score}")
            game_on = False
            break