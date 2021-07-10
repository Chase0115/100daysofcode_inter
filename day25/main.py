import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# ---------------------------->
print(data["temp"].mean())

print(data["temp"].max())

# Get the data column
print(data["condition"])
# This is the same way to print conditions
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 1.8 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv") # Create csv file