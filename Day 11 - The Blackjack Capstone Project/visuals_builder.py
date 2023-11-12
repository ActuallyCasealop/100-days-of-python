logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

rules_prompt = """
we have but only one house rule! "The size of the deck is unlimited."

the rest goes for the standard rule of blackjack:
    1. beat the dealers cards without going over 21.
    2. you'll recieve 2 cards on the first round, and add them up.
    3. cards (2-10) has their face value, ace is 11, and face cards are 10.
    4. the dealer also draw two cards. the aim is to beat his hand.
    5. type "hit" if you want to be dealt with another card.
    6. type "stand" if you want to keep your current hand.
    7. "bust" is a term when the total sum of the cards exceed 21, an instant lose.
    8. the winner is whoever has the highest hand without going bust.
"""

start = "[Start] [Exit]\n>>> "
options = "[Hit] [Stand]\n>>>: "
invalid_entry = "Invalid entry; please choose between the two."

suits = ["♣", "♦", "♥", "♠"]

playing_cards = {
    'A':11,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'K':10,
    'Q':10,
    'J':10
}

