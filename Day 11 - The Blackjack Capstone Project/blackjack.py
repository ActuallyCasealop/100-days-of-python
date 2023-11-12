from visuals_builder import *
import random
import os


def random_card():
    return random.choice(list(playing_cards.keys()))

def random_suit():
    return random.choice(suits)

def spacing(card):
    if len(card) == 1:
        return f"{card} "
    else:
        return card
    
def double_cards_display(first_card, second_card, player):
    spacing_FC = spacing(first_card)
    spacing_SC = spacing(second_card)

    second_suit = ""
    if player == "player":
        second_suit = random_suit()
    else:
        second_suit = dealer_sc_suit
    return print(f"""
┌─────────┐     ┌─────────┐
│{spacing_FC}       │     │{spacing_SC}       │
│         │     │         │
│         │     │         │
│    {random_suit()}    │     │    {second_suit}    │
│         │     │         │
│         │     │         │
│       {spacing_FC}│     │       {spacing_SC}│
└─────────┘     └─────────┘
""")


def dealer_cards_display():
    spacing_SC = spacing(dealer_sc)

    return print(f"""
┌─────────┐     ┌─────────┐
│░░░░░░░░░│     │{spacing_SC}       │
│░░░░░░░░░│     │         │
│░░░░░░░░░│     │         │
│░░░░░░░░░│     │    {dealer_sc_suit}    │
│░░░░░░░░░│     │         │
│░░░░░░░░░│     │         │
│░░░░░░░░░│     │       {spacing_SC}│
└─────────┘     └─────────┘
""")

def hit(player):
    global player_hand_value
    global dealer_hand_value

    hit_card = random_card()
    if player == 'player':
        player_hand_value += playing_cards[hit_card]
        print(f"Your new hand value: {player_hand_value}")
    else:
        dealer_hand_value += playing_cards[hit_card]
        print(f"The dealers new hand value: {dealer_hand_value}")

    return print(f"""
        ┌─────────┐
        │{spacing(hit_card)}       │
        │         │
        │         │
        │    {random_suit()}    │
        │         │
        │         │
        │       {spacing(hit_card)}│
        └─────────┘
        """)

game_on = True

player_fc,player_sc = random_card(), random_card()
dealer_fc, dealer_sc = random_card(),random_card()

player_hand_value = playing_cards[player_fc] + playing_cards[player_sc]
dealer_hand_value = playing_cards[dealer_fc] + playing_cards[dealer_sc]

dealer_sc_suit = random.choice(suits)

print(logo)

print(rules_prompt)

while True:
    if game_on == False:
        break
    else:
        user_input = input(start).lower()
        if user_input == 'start':
            os.system('cls')
            print(f"Your hand value: {player_hand_value}")
            double_cards_display(player_fc,player_sc,'player')
            print(f"The dealers hand: ????, {dealer_sc}")
            dealer_cards_display()
            while game_on:
                user_input = input(options).lower()
                if user_input == 'hit':
                    hit('player')
                    if player_hand_value > 21:
                        print("You have exeeded 21; you lose.")
                        game_on = False
                elif user_input == 'stand':
                    print(f"Dealers hand value: {dealer_hand_value}")
                    double_cards_display(dealer_fc,dealer_sc,'dealer')

                    while dealer_hand_value < 16:
                        hit('dealer')
                        if dealer_hand_value > 21:
                            print("The dealer exceeded 21; you won.")
                            game_on = False
                    if player_hand_value > dealer_hand_value:
                        print("Your hand is of higher value; you won.")
                    elif dealer_hand_value > player_hand_value:
                        print("The dealers hand is of higher value; you lose.")
                    else:
                        print("Equal similar hand value; it was a draw.")
                    game_on = False
                else:
                    print(invalid_entry)
        elif user_input == 'exit':
            break
        else:
            print(invalid_entry)