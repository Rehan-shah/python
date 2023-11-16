import json

link = input("Enter the link :")
minium_price = input("Enter the minimum price :")

config = {
    "link": link,
    "minium_price": minium_price
}



with open("config.json", "w") as doc :
    doc.write(json.dumps(config))
