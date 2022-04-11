from email.policy import default
from ensurepip import bootstrap
from enum import unique
from datetime import datetime
import sqlite3
from tkinter.tix import Form
from tokenize import String
from turtle import title
from flask import Flask,render_template,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from forms import LoginForm, RegisterForm
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.sqlite'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(20),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('post',backref='author',lazy=True)
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow )
    content=db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    
        
posts=[
    {
        "title":"Russia",
        "author":"james bengi",
        "date_posted":"jan 14 2020",
        "content":"Hey man"
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'james@gmail.com' and form.password.data =="password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)