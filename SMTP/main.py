import random
import smtplib
import datetime as dt

my_email = "Rehansnehalshah1@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password="lpcgolzzdttrxgkx")

text = None

with open('quotes.txt', "r") as doc:
    text = doc.read().split("\n")

if dt.datetime.now().weekday() == 3:
    random_quote = random.choice(text)
    connection.sendmail(from_addr=my_email,
                        to_addrs="rehan.shah@aischool.net",
                        msg=f"Subject:Hello\n\n Quote\n{random_quote}")
else:
    print('not today')
    print(dt.datetime.now().weekday())

connection.close()
