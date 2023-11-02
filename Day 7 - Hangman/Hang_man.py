import random
import os

word_choice = ["Arrival","Barbwire","String","Communication","Saturate","Heater","Floppy","Satirise","Hypnotic","Presence","Honeymoon","Decorous","Absurdly","Difficult","Activity", "Practical", "Bleakly", "Evidence", "Spurious", "Temper"]

pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

random_word = random.choice(word_choice).lower()

word_place_holder = []

for i in random_word:
        word_place_holder.append("_")

player_lives = 6
game_on = True
while game_on:
        print(pics[-player_lives-1])
        print("".join(word_place_holder))

        if "".join(word_place_holder) == random_word:
               os.system('cls')
               print("you win")
               break
        elif player_lives == 0:
            os.system('cls')
            print(f"{pics[6]}\nThe correct answer is: {random_word}.\nyou Lose.")
            break
        
        else:
            user_input = input("what letter to choose?\n>>>: ")
            os.system('cls')

            if user_input not in random_word:
                player_lives -= 1
                print(f"Incorrect letter; you have: {player_lives} attempt remaining.")

            elif user_input in word_place_holder:
                print("Word already revealead; please choose another one.")

            else:
                print("Correct letter; please choose another one.")
                for i in range(len(random_word)):
                    if random_word[i] == user_input:
                        word_place_holder[i] = user_input
                    else:
                        pass
