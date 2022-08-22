import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ")

phonetic_list = [new_dict[letter] for letter in word.upper() if letter in new_dict.keys()]
print(phonetic_list)
