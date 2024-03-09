import pandas

nato_data = pandas.read_csv(r"Day 26 - List Comprehension and the NATO Alphabet\nato_phonetic_alphabet.csv")

nato_dic = {val.letter:val.code for (key,val) in nato_data.iterrows()}

def generate():
    user_input = input("Enter the word to be converted:\n>>>: ").upper()
    try:
        result = [nato_dic[i] for i in user_input]
    except KeyError:
        print("Only string characters are allowed.")
        generate()
    else:
        print(result)
generate()