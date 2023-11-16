
from flask import Flask , render_template, request
app = Flask(__name__)
import random
import datetime
import requests



@app.route("/")
def hello_world():
    return render_template("index.html" , random_number = random.randint(1,100) , year = datetime.datetime.now().year)

@app.route("/guess/<name>")
def name(name):
    res_age = requests.get(f"https://api.agify.io/?name={name}")
    res_age = res_age.json()

    res_gender = requests.get(f"https://api.genderize.io?name={name}")
    res_gender = res_gender.json()

    return render_template("guess.html" , name = name , age = res_age["age"] , gender = res_gender["gender"] )


def blog():
    return "h1"


if __name__ == "__main__":
   app.run(debug=True) 
