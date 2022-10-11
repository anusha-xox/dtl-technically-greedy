from flask import Flask, render_template, redirect, url_for, request, Response
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import datetime
import smtplib
from form_data import LoginForm, StudentForm, Evaluate, AddBook

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), unique=True, nullable=False)  # string
    last_name = db.Column(db.String(250), nullable=False)  # string
    grade = db.Column(db.String(500), nullable=False)  # string
    age = db.Column(db.Integer, nullable=True)  # integer
    level_assigned = db.Column(db.String(50), nullable=True)  # string
    img_url = db.Column(db.String(250), nullable=True)
    total_points = db.Column(db.Integer, nullable=True)
    badge = db.Column(db.String, nullable=True)
    no_of_writeups = db.Column(db.Integer, nullable=True)
    current_book = db.Column(db.String(2500), nullable=True)
    past_books = db.Column(db.String(2500), nullable=True)
    volunteer_email = db.Column(db.String(250), nullable=False)


# db.create_all()

@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/knap')
def knap():
    return render_template("knap_details.html")


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")


@app.route('/', methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.username.data == 'student@email.com' and login_form.password.data == 'ab':
            return render_template('index.html')

    return render_template('login.html', form=login_form)


@app.route('/view-students')
def view_students():
    return render_template("view_students.html")


@app.route('/aditi')
def aditi():
    return render_template("aditi.html")


@app.route('/ajay')
def ajay():
    return render_template("ajay.html")


@app.route('/kumar')
def kumar():
    return render_template("kumar.html")


@app.route('/edit-student')
def edit_student():
    form = StudentForm()
    if form.validate_on_submit():
        return redirect(url_for('view_students'))
    return render_template("edit-student.html", form=form)


@app.route('/add-student')
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        return redirect(url_for('view_students'))
    return render_template("add-student.html", form=form)


@app.route('/videos')
def videos():
    return render_template('level1.html')


@app.route("/Djkistras")
def dij():
    return render_template('dij.html')


if __name__ == "__main__":
    app.run(debug=True)
