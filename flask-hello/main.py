
from logging import debug
from flask import Flask
import random

app = Flask(__name__)



random_int = random.randint(0,9)

@app.route('/')
def hello_world():
    return '<h1> Gusess a number between 0 and 9 </h1>'\
            '<img src="https://media4.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif?cid=ecf05e47m0qq2f2v4e2d37lw8cvj8rv6nefqle9uas9y2kiu&ep=v1_gifs_search" width=400/>'

@app.route("/<int:number>")
def gusses(number):
    global random_int
    if number > random_int:
        return "<h1 style='color:blue ; font-size: 30px'> sorry, your number is too high </h1>"\
                "<img src='https://media.giphy.com/media/3o6ztao9bzhcojmerm/giphy.gif' width=400/>"
    elif number < random_int:
        return "<h1 style='color:red; font-size: 30px'> sorry, your number is too low</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=400/>"
    else:
        random_int = random.randint(0,9)
        return "<h1 style='color:green; font-size: 30px'> Wow you Gusess , game is restarted</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=400/>"

@app.post("/")
def glass():
    return "hello"




if __name__ == '__main__':
    app.run(debug=True)
