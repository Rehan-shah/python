from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

from sqlalchemy import except_, func
import sqlite3
from sqlalchemy.event import api

from sqlalchemy.orm.query import sql
from sqlalchemy.sql.functions import current_user
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)



@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.get("/random")
def get_rnd_cafe():
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe).order_by(func.random())).scalar().__dict__

        cafes.pop("_sa_instance_state")

    cafe = {"cafe": cafes}
    return jsonify(cafe)

@app.get("/all")
def get_all_cafe():
    # Step 1: Connect to the SQLite database
    connection = sqlite3.connect("./instance/cafes.db")
    cursor = connection.cursor()

    # Step 2: Execute a SELECT query to retrieve data
    query = f"SELECT * FROM Cafe"
    cursor.execute(query)

    # Step 3: Fetch all the data and store it in a list of {dictionaries
    data = []
    columns = [col[0] for col in cursor.description]
    for row in cursor.fetchall():
        data.append(dict(zip(columns, row)))

    # Step 4: Close the database connection and return the data
    cursor.close()
    connection.close()
    return data

@app.get("/search")
def get_cafe():

    connection = sqlite3.connect("./instance/cafes.db")
    cursor = connection.cursor()
    name = request.args.get("loc")
    print(name)
    # Step 2: Execute a SELECT query to retrieve data
    try:
        query = f'SELECT * FROM cafe WHERE location LIKE "{name}"'
        cursor.execute(query)
    
        # Step 3: Fetch all the data and store it in a list of {dictionaries
        data = []
        columns = [col[0] for col in cursor.description]
        print(columns)
        for row in cursor.fetchall():
            data.append(dict(zip(columns, row)))
    except :
        data = {"error":"error could not find cafe"}
    # Step 4: Close the database connection and return the data
    if len(data) == 0:
        return {"error":"error could not find cafe"} ,404
    cursor.close()
    connection.close()
    return data



## HTTP POST - Create Record
@app.post("/add")
def add_cafe():
    connection = sqlite3.connect("./instance/cafes.db")
    cursor = connection.cursor()

    query = 'SELECT * FROM cafe'
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]

    print(columns)
    dic={}
  
    for n in columns:
        dic[n] = request.form.get(n)
        if not (n == "id") and dic[n] == None :
            print(n)
            return {"response": {"error": "not all key porovided"}} ,403

    print(dic)
    query = 'INSERT INTO cafe (name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(query, (dic["name"], dic["map_url"], dic["img_url"], dic["location"], dic["seats"], dic["has_toilet"], dic["has_wifi"], dic["has_sockets"], dic["can_take_calls"], dic["coffee_price"]))
    connection.commit()
    cursor.close()
    connection.close()

    return {"response": {"succes": "add recored"}} ,200
## HTTP PUT/PATCH - Update Record
@app.patch("/upadate-price/<int:id>")
def change_price(id):
    connection = sqlite3.connect("./instance/cafes.db")
    cursor = connection.cursor()
    new_price = request.args.get('new_price')
    if new_price == None:
        return {"error": {
            "Wrong entriey": "could not find new price "
        }}, 402
    try: 
        query = 'UPDATE cafe SET coffee_price = ? WHERE id = ? '
        cursor.execute(query,(new_price , id))
        connection.commit()
    except Exception as e:
        print(e)
        return {"error": {
            "Wrong entriey": "could not find id "
        }}, 404
    cursor.close()
    connection.close()

    return {"response": {"succes": "Updated recored"}} ,200

## HTTP DELETE - Delete Record

@app.delete("/remove/<int:id>")
def remove_report(id):
    connection = sqlite3.connect("./instance/cafes.db")
    cursor = connection.cursor()
    api_key = request.headers.get("api_key")
    if not api_key == "TopSecretAPIKey":
        return {"error": {
            "unauthorize": "api key not coorect"
        }} , 401

    try:
        query = 'DELETE FROM cafe WHERE id = ?'
        cursor.execute(query,(id,))
        connection.commit()
    except Exception as e:
        print(e)
        return {"error": {
            "Wrong entriey": "could not find id "
        }}, 404
    cursor.close()
    connection.close()
    return {"response": {"succes": "Deleted recored"}} ,200

if __name__ == '__main__':
    app.run(debug=True)
