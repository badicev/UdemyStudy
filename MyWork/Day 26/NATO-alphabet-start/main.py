#----------------------------------------------------------------------------------------------------------------#
''' NATO Alphabet Project '''
import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in nato.iterrows()}

# print(dict)

# 2nd part

user_word = input("Say something: ").upper()
list = [dict[letter] for letter  in user_word]
print(list)

