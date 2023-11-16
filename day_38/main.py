from collections.abc import Iterator
import requests
from datetime import datetime 


descripe = input('What eerise hav n')

headers = {
    "x-app-id":"b74dfa5f",
    "x-app-key":"1d25a38a0684b9bdb1df207364708b49"
}

json = {
 "query":"ran 3 miles",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}


res = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise" , json=json , headers=headers)
res.raise_for_status()
res = res.json()

print(res)

def add_row(content):
    headers_sheety= {
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"
    }
    url = 'https://api.sheety.co/d6a4515d2941cd6850b63c72e83277ac/myWorkouts/workouts'
    res = requests.post(url=url, json=content , headers=headers_sheety)
    res.raise_for_status()
    print(res.text)

for exercise in  res["exercises"]:
    body ={"workout": {
        "date":datetime.now().strftime("%d/%m/%Y"),
        "time":datetime.now().strftime("%H:%M:%S"),
        "exercise":exercise["user_input"].title(),
        "duration":exercise["duration_min"],
        "calories":exercise["nf_calories"]
    }}
    print(body)
    add_row(body)

url = 'https://api.sheety.co/d6a4515d2941cd6850b63c72e83277ac/myWorkouts/workouts'

def give():
    res = requests.get(url=url)
    res.raise_for_status()
    return res.json()


print(give())
