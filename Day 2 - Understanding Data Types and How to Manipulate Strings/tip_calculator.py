#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
user_bill = int(input("Greetings! this is a tip calculator.\nPlease enter the bill ammount.\n>>>: "))
total_people = int(input("Please enter the ammount of people the bill should be split up with:\n>>>: "))

bill = "{:.2f}".format(round((user_bill / total_people),2))

print(f"The total bill to be split up between {total_people} people is: {bill} Pesos.")