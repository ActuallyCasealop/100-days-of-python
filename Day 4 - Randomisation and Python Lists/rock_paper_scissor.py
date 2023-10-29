import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
RPS_choices = [rock,paper,scissors]
user_RPS = ["rock","paper","scissors"]

user_input = int(input("Lets play Rock, Paper, Scissor! Ready?\nrock [1], paper [2], scissors [2]\n>>>: "))-1

random_number = random.randint(0,2)

print("I choose:")
print(RPS_choices[random_number])
print(f"you Choose:")
print(RPS_choices[user_input])

if user_input == 0:
    if random_number == 0:
        print("A Rock and a Rock! its a Draw.")
    elif random_number == 1:
        print("A Paper and a Rock! I Win.")
    else:
        print("A Scissor and a Rock! I Lose.")
elif user_input == 1:
    if random_number == 0:
        print("A Rock and a Paper! I lose.")
    elif random_number == 1:
        print("A Paper and a Paper! Its a Draw.")
    else:
        print("A Scissor and a paper! I win.")
elif user_input == 2:
    if random_number == 0:
        print("A Rock and a Scissor! I Win.")
    elif random_number == 1:
        print("A Paper and a Scissor! I Lose.")
    else:
        print("A Scissor and Scissor! its a Draw.")