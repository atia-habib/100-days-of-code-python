import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# Create a list of phonetic words
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
