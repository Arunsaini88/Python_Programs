import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}


# Using Recursion in this program
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [data_dict[letters] for letters in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()