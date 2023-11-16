from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()

ckeditor = CKEditor()
db.init_app(app)
ckeditor.init_app(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()


class Post(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField('Body' ,validators=[DataRequired()])  # <--
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    with app.app_context():
        list = db.session.query(BlogPost).all()
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = list
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/posts/<int:post_id>')
def show_post(post_id):

    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.get("/edit-post/<int:post_id>")
def change_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = Post(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    return render_template("make-post.html" , heading="Edit post" , form=edit_form)
# TODO: add_new_post() to create a new blog post
@app.post("/edit-post/<int:post_id>")
def change_post_b(post_id):
    form = Post()
    post = db.get_or_404(BlogPost, post_id)
    post.title = form.title.data
    post.subtitle = form.subtitle.data
    post.author = form.author.data
    post.img_url = form.img_url.data
    post.body = form.body.data                     
    db.session.commit()
    return redirect("/")

@app.get("/new-post")
def edit_post():
    form = Post()
    return render_template("make-post.html" ,form=form , heading="New post")

@app.post("/new-post")
def post_post():

    form = Post()

    new_post = BlogPost(
    date=date.today().strftime("%B %d, %Y"),
    title=form.title.data,
    subtitle=form.subtitle.data,
    author=form.author.data,
    img_url=form.img_url.data,
    body=form.body.data,
)
    db.session.add(new_post)
    db.session.commit()

    return redirect("/")

# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database
@app.get("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/")


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
