#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

guest_names = open(r"Day 24 - Files, Directories and Paths\Input\Names\invited_names.txt",mode='r+').readlines()

for name in guest_names:
    with open(f"Day 24 - Files, Directories and Paths\Output\ReadyToSend\letter_for_{name.strip()}",mode='w') as letter_format:
        starting_letter = open("Day 24 - Files, Directories and Paths\Input\Letters\starting_letter.txt",mode='r').read()
        starting_letter = starting_letter.replace('[name]',name.strip())
        letter_format.write(starting_letter)
        print('Process Finished')