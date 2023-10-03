import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ")
    try:
        phonetic_list = [new_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Sorry, only the letters in the alphabet please.\n")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()

