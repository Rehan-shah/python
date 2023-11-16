from os import walk
from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy.engine import url
from wtforms.fields import IntegerField
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, validators, widgets
from wtforms.validators import DataRequired, NumberRange
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float , nullable=True)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500) , nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

class MoiveForm(FlaskForm):
    rating = IntegerField(validators=[NumberRange(min=1,max=10),DataRequired()] , label="Your rating out of 10" ) 
    review = StringField(validators=[DataRequired()] ,label ="Your review" )
    submit = SubmitField('Done' )




@app.route("/")
def home():
    with app.app_context():
        movies = db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html" , moives=movies)

@app.get("/edit/<int:id>")
def edit(id):
    form = MoiveForm()
    with app.app_context():
        movies = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar().__dict__
    return render_template("edit.html" , form=form , moive=movies["title"])

@app.post("/edit/<int:id>")
def edit_post(id):
    form = MoiveForm()
    with app.app_context():
        movies = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movies.rating = form.rating.data
        movies.review = form.review.data
        db.session.commit()
    return redirect(url_for('home'))

@app.get("/delete/<int:id>")
def delete(id):
    with app.app_context():
        moives = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        db.session.delete(moives)
        db.session.commit()
    return redirect(url_for('home'))


@app.get('/add')
def add():
    return render_template("add.html")

@app.post("/add")
def add_post():
    title = request.form["title"]
    params ={
        "query":title,
        "api_key":"dc137265e1b2a220f7e1bbb2142ffa93"
    }
    res = requests.get("https://api.themoviedb.org/3/search/movie" , params=params)
    movies = []
    for movie in res.json()["results"]:
        movies.append((movie["original_title"] , movie["id"] , movie["release_date"]))


    return render_template("select.html" , movies=movies)

@app.get("/select/<int:id>")
def select(id):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzEzNzI2NWUxYjJhMjIwZjdlMWJiYjIxNDJmZmE5MyIsInN1YiI6IjY0YzRiNzc2NjNhYWQyMDIwYzNhOTNjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9nXtFFqk4_NNGaQouqAL2RVI4s72EQOkbhhaULyC-SY"
    }
    res = requests.get(f"https://api.themoviedb.org/3/movie/{id}"  , headers=headers)
    res = res.json()
    with app.app_context():
        new_movie = Movie(title=res["original_title"] , year=res["release_date"] , description=res["overview"]  , ranking=res["vote_count"]  , img_url="https://image.tmdb.org/t/p/w500"+res["poster_path"])
        db.session.add(new_movie)
        db.session.commit() 
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
