import smtplib
from bs4 import BeautifulSoup
import requests
import json


link = None
price = None

with open("config.json" , "r") as doc:
    data = doc.read()
    data = json.loads(data)
    link = data["link"]
    price = data["minium_price"]


headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Cookie":"PHPSESSID=3ff4df7a76d16bf885948ea23595106f"
}
html_unparse = requests.get(url=link , headers=headers)


soup = BeautifulSoup(html_unparse.content, "html.parser")


price = soup.find("div" , class_= "_30jeq3 _16Jk6d")
price = price.get_text()
price = price.replace("₹" , "")
price = price.replace("," , "")
price = int(price)  

title = soup.find("span" , class_="B_NuCI")
title = title.get_text()


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login("reh" , )
