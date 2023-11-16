from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

db = SQLAlchemy()




app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new_books_collection.db"

db.init_app(app)




class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String , nullable=False , unique=True)
    author = db.Column(db.String , nullable=False)
    rating = db.Column(db.Integer , nullable=False)


def create_user(title:str , author:str , rating:str):
    with app.app_context():
        user = User(title=title , author=author, rating=rating)
        db.session.add(user)
        db.session.commit()

def reade_all():
    with app.app_context():
        result = db.session.execute(db.select(User).order_by(User.title))
        res = result.scalars()
        return res.all()



@app.route('/')
def home():
    all_books = reade_all()
    return render_template("index.html" , all_books=all_books)

@app.route("/add")
def add():
    return render_template("add.html")

@app.post("/add")
def add_book():
    name = request.form.get("name")
    author = request.form.get("author")
    rating = request.form.get("rating")
    create_user(title=name , author=author , rating=rating)

    return redirect(url_for("home"))

@app.get("/edit/<int:id>")
def edit(id):
    return render_template("edit.html" , id=id , name=User.query.get(id).title , rating=User.query.get(id).rating)

@app.post("/edit/<int:id>")
def post_edit(id):
    with app.app_context():
        user = db.session.execute(db.select(User).where(User.id == id)).scalar_one()
        user.rating = request.form["rating"]
        db.session.commit()
    return redirect(url_for("home")) 

@app.get("/remove/<int:id>")
def remove(id):
    with app.app_context():
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
