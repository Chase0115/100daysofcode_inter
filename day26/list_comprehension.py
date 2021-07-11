# List Comprehension

numbers = [1, 2, 3]
# --> new_list = [new_item for item in list]
new_numbers = [n + 1 for n in numbers]

# Apply to string

name = "Chase"
new_list = [letter for letter in name]

new_number_list = [n * 2 for n in range(1,5)]

# Another List Comprehension
names = ["Arizona", "California", "Arkansas", "Alaska", "Cola", "Alex", "Dim"]
# --> new_list = [new_item for item in list if condition]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]

