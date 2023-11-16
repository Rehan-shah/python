from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField , URLField, validators  
from wtforms.validators import DataRequired , URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


choices = [(0 ,0),(1,1) , (2,2),(3,3),(4,4),(5,5)]

def return_emoji_chocie(emoji:str):
    choices = []
    for n in range(0,6):
        str = ""
        for i in range(0,n):
            str += emoji
        if n== 0:
            str = "✘"
        choices.append((str , str))
    return choices



class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location', validators=[DataRequired() ,URL()]) 
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=return_emoji_chocie("☕️"), validators=[DataRequired()])
    wifi_rating = SelectField("Wifi rating", choices=return_emoji_chocie("💪"), validators=[DataRequired()])
    power_outlet = SelectField("Power outlet", choices=return_emoji_chocie("🔌"), validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add' ,methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    if form.validate_on_submit():
        with open("cafe-data.csv" ,"a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([form.cafe.data, form.location.data, form.open_time.data, form.close_time.data, form.coffee_rating.data, form.wifi_rating.data, form.power_outlet.data])

    return render_template('add.html', form=form)



@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows )



if __name__ == '__main__':
    app.run(debug=True)
