# with open("./weather_data.csv") as weater_info:
#     weather = weater_info.readlines()
#     new_weather_data = []
#     for weather_data in weather:
#         split_weather_data = weather_data.split(",")
#         split_weather_data[2] = split_weather_data[2].strip()
#         new_weather_data.append(split_weather_data)
#
#     print(new_weather_data)

# Use csv

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures

# Use Pandas

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])