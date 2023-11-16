import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

today_dt = datetime.now().date()

# Calculate tomorrow's date
params= {
    'symbol':STOCK,
    'apikey':'RKX2S94XRXAW5RAQ'
}

res = requests.get(url='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED',params=params).json()


stock_price = res['Time Series (Daily)']
today = (today_dt - timedelta(days=1)).strftime('%Y-%m-%d')
yesterday = (today_dt - timedelta(days=2)).strftime('%Y-%m-%d')

diffrence = (float(stock_price[today]["4. close"])-float(stock_price[yesterday]["4. close"]))/float(stock_price[yesterday]["4. close"])
diffrence = round(diffrence*100 , 1)

def send_message(msg):
    account_sid = 'ACd92519308777456fc14f8bad41c159f1'
    auth_token = '875f4a102a8837d3d2301693f8372ab6'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=msg,
        to='whatsapp:+917575815632'
    )


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
params = {
    'q': STOCK,
    "from":yesterday,
    'to':today,
    'sortBy': "popularity",
    'apiKey': '10b0f642dd5d4b118c7a0258797c7baf'
}

# new_res = requests.get(f'https://newsapi.org/v2/everything?q={STOCK}&from=yesterday&to=today&sortBy=popularity&apiKey=10b0f642dd5d4b118c7a0258797c7baf')
new_res = requests.get(url='https://newsapi.org/v2/everything' , params=params)
new_res.raise_for_status()

json = new_res.json()
json = json["articles"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
up_or_down = None
if diffrence >= 0:
    up_or_down ='🔺'
else:
    up_or_down = '🔻'
change_price = f'{STOCK}: {up_or_down} {diffrence}%'


if abs(diffrence) > 5:
    for i in range(1,3):
        send_message(f"""
    {change_price}
Headline: {json[i]["title"]}
description: {json[i]["description"]}
        
Headline: {json[i]["title"]}
description: {json[i]["description"]}
        
Headline: {json[i]["title"]}
description: {json[i]["description"]}
        """)
else:
      send_message(f"""
    {change_price}
Headline: {json[0]["title"]}
description: {json[0]["description"]} """)

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

