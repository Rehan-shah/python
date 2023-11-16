from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blogs = requests.get("https://api.npoint.io/20867b47f8a8254b616d")
    blogs = blogs.json()
    return render_template("index.html" , blogs=blogs)

@app.route("/blog/<int:id>")
def blog(id):
    blogs = requests.get("https://api.npoint.io/20867b47f8a8254b616d")
    blogs = blogs.json()
    return render_template("post.html",blog=blogs[id-1])



if __name__ == "__main__":
    app.run(debug=True)
