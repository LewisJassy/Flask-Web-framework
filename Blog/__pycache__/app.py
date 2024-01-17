from flask import Flask, render_template, url_for, flash, redirect
from blog.form import RegstrationForm, LoginForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = 'c6d75c5b3fe288fa1ced520a011e19'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)
from blog.models import User, Post

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegstrationForm()
    if form.validate_on_submit():
        flash("Registration successful!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit:
        if form.email.data == 'lewisjassy@gmail.com' and form.password.data == 'lewisjassy':
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template("login.html", title="Login", form=form)
