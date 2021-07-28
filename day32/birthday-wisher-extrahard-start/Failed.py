##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
from random import randint
import smtplib

# 1. Update the birthdays.csv
with open("birthdays.csv") as birthday_data:
    df = pd.read_csv(birthday_data)
    birthday_data.close()
    df['new_day'] = list(zip(df.month, df.day))
    birthday_list = df['new_day'].tolist()

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
today_tuple = (today.month, today.day)
if today_tuple in birthday_list:
    name = df.name[df['new_day'] == today_tuple]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
global file_path
file_path = f"letter_templates/letter_{randint(1,3)}.txt"

with open(file_path, 'r') as letter:
    new_text_content = ''
    target_word = '[NAME]'
    new_world = name.to_string()
    lines = letter.readlines()
    for i, l in enumerate(lines):
        new_string = l.strip().replace(target_word, new_world)
        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'




# 4. Send the letter generated in step 3 to that person's email address.


my_email = "smtppythontest.sample@gmail.com"
password = "qrpqrp0101"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sgh0115@gmail.com",
        msg=f"Subject:Happy birthday\n\n {new_text_content}")
    connection.close()



