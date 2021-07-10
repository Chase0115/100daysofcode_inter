# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()


# with open("my_file.txt", mode="a") as file:
#     file.write("New text.")
#     file.close()

with open("my_file2.txt", mode="w") as file:
    file.write("New text.")
    file.close()