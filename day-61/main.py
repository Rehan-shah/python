from flask import Flask, render_template, request
from form import SignUpForm 
from flask_bootstrap import Bootstrap5



app = Flask(__name__)


bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login" , methods=["GET" ,"POST"])
def login():
    print("hii")
    form = SignUpForm() 
    if form.validate_on_submit() :
        if form.username.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else :
            return render_template("denied.html")
    return render_template("login.html" , form = form)



if __name__ == '__main__':
    app.run(debug=True)
