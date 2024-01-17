from blog.form import RegstrationForm, LoginForm
from flask import render_template, url_for, flash, redirect
from blog.models import User, Post
from blog import app
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