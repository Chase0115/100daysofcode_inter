import smtplib
import datetime as dt
import random


MY_EMAIL = "smtppythontest.sample@gmail.com"
PASSWORD = "qrpqrp0101"

with open("quotes.txt", "r") as data:
    quote_list = []
    for line in data.readlines():
        new_line = line.strip()
        quote_list.append(new_line)

    data.close()
now = dt.datetime.now()
current_day = now.weekday()
print(current_day)


if current_day == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="sgh0115@gmail.com",
            msg=f"Subject:motivation quote\n\n {random.choice(quote_list)}"
        )
        connection.close()





