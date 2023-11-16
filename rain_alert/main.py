import requests
from twilio.rest import Client
import os

print(os.environ.get('OWM_API'))
params = {
    'lat': 23.033863,
    'lon': 72.58502,
    'exclude':'current,minutely,daily',
    "appid": os.environ.get('OWM_API')
}

res = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=params)
res.raise_for_status()
res = res.json()

res = res["hourly"]

msg = 'It will not rain today'

for hour in res:
    if hour["weather"][0]["id"] < 700 :
        msg = 'Yes it will rain today'
        break;

account_sid = 'ACd92519308777456fc14f8bad41c159f1'
auth_token = '875f4a102a8837d3d2301693f8372ab6'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=msg,
  to='whatsapp:+917575815632'
)

print(message.sid)
