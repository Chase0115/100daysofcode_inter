student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#   Access key and value
#     print(key)
#     print(value)
#     pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # print(index)
    # print(row)
    #Access row.student or row.score
    # print(row.student)
    # print(row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# ---------------------------------------------------------------------------
# -----------------------Start Coding----------------------------------------
# ---------------------------------------------------------------------------

#TODO 1. Create a dictionary in this format:

with open("nato_phonetic_alphabet.csv") as data:
    nato_data = pandas.read_csv(data)
    # nato_dict = pandas.read_csv(nato_data, index_col=0, squeeze=True).to_dict()
    nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
    print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter the a word : ").upper()
input_letters = [letter for letter in user_input]
result = [nato_dict[letter] for letter in input_letters]
print(result)