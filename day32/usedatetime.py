import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2021:
    print("Wear a face mask")
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1993, month=1, day=15, hour=4)
print(date_of_birth)