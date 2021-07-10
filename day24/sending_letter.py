PLACEHOLDER = "[name]"

with open("./names/names.txt") as names_file:
    names = names_file.readlines()
    names_file.close()

with open("./letters/letter.txt") as letter_file:
    letter = letter_file.read()
    letter_file.close()


for name in names:
    new_name = name.strip()
    with open(f"./letter_output/{new_name}'s letter.txt", "w") as sending_letter:
        changed_name = letter.replace(PLACEHOLDER, f"{new_name}")
        sending_letter.write(f"{changed_name}")