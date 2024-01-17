from blog.form import RegstrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, get_flashed_messages
from blog.models import User, Post
from blog import app
@app.route('/')
def home():
    message = get_flashed_messages(with_categories=True)
    return render_template("home.html", message=message)

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        if form.email.data == 'lewisjassy@gmail.com' and form.password.data == 'lewisjassy':
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template("login.html", title="Login", form=form)