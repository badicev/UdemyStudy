# ----------------------------------------------------------------------------------------------------------------#
''' NATO Alphabet Project '''
import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in nato.iterrows()}


# print(dict)

# 2nd part
def generate_phonetic():
    user_word = input("Say something: ").upper()

    try:
        output_list = [dict[letter] for letter in user_word]

    except KeyError:
        print("Sorry, only letters in the alphabet.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
