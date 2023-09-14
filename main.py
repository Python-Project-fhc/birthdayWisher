import datetime as dt
import random
import smtplib

import pandas

my_email = ""
password = ""  # APP Password

# 2. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filepath) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!!\n\n{content}")
