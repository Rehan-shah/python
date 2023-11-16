from functools import reduce
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory , get_flashed_messages
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

is_registered = False

# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 


@app.route('/')
def home():
    return render_template("index.html" , logged = is_registered)

@app.get('/register')
def register():
    return render_template("register.html" , logged = is_registered)

@app.post("/register")
def register_post():
    global is_registered
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    password = generate_password_hash(password=password , method="pbkdf2" , salt_length=8 )  
    db = sqlite3.connect("./instance/users.db")
    try :
        cursor = db.cursor()
        cursor.execute("INSERT INTO user (name, email, password) VALUES (?, ?, ?)",(name, email, password))
        db.commit()
        is_registered = True
        return render_template("secrets.html" , name=name , logged = is_registered)
    except :
        flash("Record already exists")
        return redirect("/register")
    cursor.close()
    db.close()
    






@app.route('/login'  ,methods=["POST","GET"])
def login():
    global is_registered
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user == None:
            flash('Email not found')
        else :
            password_true = check_password_hash(user.password, request.form.get("password"))
            if not password_true:
                flash("Invalid password")
            else:

                is_registered = True
                return redirect("/secrets")

    return render_template("login.html" , logged = is_registered)



@app.route('/secrets')
def secrets():
    return render_template("secrets.html" , logged = is_registered)


@app.route('/logout')
def logout():
    global is_registered
    is_registered = False
    return redirect("/")


@app.route('/download')
def download():
    return send_from_directory("./static/files/" ,"cheat_sheet.pdf" ) 

if __name__ == "__main__":
    app.run(debug=True)
