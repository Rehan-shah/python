##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import random as rng
import datetime as dt
import smtplib as smtp

df = pd.read_csv("birthdays.csv")

today_date = dt.datetime.now()

hello = [
    True 
] * 5

for index, row in df.iterrows():
    if row["month"] == today_date.month and row["day"] == today_date.day:
        random_num = rng.randint(1, 3)
        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="Rehansnehalshah1@gmail.com", password="lpcgolzzdttrxgkx")
            file = open(f"letter_templates/letter_{random_num}.txt", "r")
            file = file.read()
            file = file.replace("[NAME]", row["name"])

            connection.sendmail(from_addr="Rehansnehalshah1@gmail.com", to_addrs=row["email"],
                                msg=f"Subject:Happy birthday 10\n\n{file}")
