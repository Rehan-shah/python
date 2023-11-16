# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


def run():
    # TODO 1. Create a dictionary in this format:
    file = pandas.read_csv("nato_phonetic_alphabet.csv")

    photic_dic = {row.letter: row.code for (_i, row) in file.iterrows()}

    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.

    words = input("Which word would like us to convert to photeitc list: ")
    try:
        print([photic_dic[char.upper()] for char in words])
    except KeyError:
        print("Sorry pllease only enter alpahabterss")
        run()

run()
