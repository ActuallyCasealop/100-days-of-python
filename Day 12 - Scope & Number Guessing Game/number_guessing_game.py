import random

random_choice = random.choice(range(0,100))

print("Welcome to the number guessing game!\nI'm thinking of a number from 1-100; can you guess which one it is?")
while True:
    user_input = input("Choose your difficulty: [Easy] [medium] [hard]\n>>>: ").lower()
    if user_input == 'easy':
        user_attempt = 10
        break
    elif user_input == 'medium':
        user_attempt = 6
        break
    elif user_input == 'hard':
        user_attempt = 3
        break
    else:
        print("Invalid Entry; please type only one of the following.")


while user_attempt != 0:
    user_input = int(input("Guess the number:"))
    user_attempt -= 1
    if user_input > random_choice:
        print("Lower")
    elif user_input < random_choice:
        print("Higher")
    else:
        print(f"Correct! the correct number is: {random_choice}")
        break
else:
    print(f"You Lose! the correct answer is: {random_choice}")