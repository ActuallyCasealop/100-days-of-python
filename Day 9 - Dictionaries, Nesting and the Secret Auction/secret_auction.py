import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bidders = []

Auction_on = True

print("Welcome to the Auction! Please type your name to proceed.")

while Auction_on:
    print(logo)
    bidder_name = input("Bidder Name:\n>>>: ")
    bid_ammount = int(input("Ammount:\n>>>: "))

    bidders.append({
        "name":bidder_name,
        "bid ammount":bid_ammount
    })

    auction_continue = input("Is there another bidder? [Y] [N]\n>>>: ")
    if auction_continue.lower() == 'y':
        os.system('cls')
        continue
    else:
        break

bidder = []
for entry in bidders:
    if not bidder:
        bidder = entry
    elif entry["bid ammount"] > bidder["bid ammount"]:
        bidder = entry
    else:
        pass
    
print(f"The auction have concluded! {bidder['name']} has the highest bid of: {bidder['bid ammount']} ")