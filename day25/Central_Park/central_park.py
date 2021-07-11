import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")
table = pd.DataFrame(data)

gray_color = len(table[table["Primary Fur Color"] == "Gray"])
red_color = len(table[table["Primary Fur Color"] == "Cinnamon"])
black_color = len(table[table["Primary Fur Color"] == "Black"])
color_dict = {
    "Fur Color": ["gray", "red", "black"],
    "count": [gray_color, red_color, black_color]
}

df = pd.DataFrame.from_dict(color_dict)
df.to_csv("Squirral_count.csv")
