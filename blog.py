from ensurepip import bootstrap
import sqlite3
from tkinter.tix import Form
from turtle import title
from flask import Flask,render_template,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.sqlite'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db=SQLAlchemy(app)
posts=[
    {
        "title":"Russia",
        "author":"james bengi",
        "date_posted":"jan 14 2020",
        "content":"hey man"
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/index')

def index():
    return render_template('index.html',posts=posts) 
@app.route("/login",methods=['GET','POST'])
def login():
   form =LoginForm()
   if form.validate_on_submit: 
       if form.email.data=="jamesbengi21@gmai"and form.password.data==1234:
           flash(f'you have been logged in','success')
           return redirect(url_for('home'))
       else:
           flash('login unseccessful. please check your email and password','danger')
   return render_template('login.html',form=form)
@app.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit:
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)