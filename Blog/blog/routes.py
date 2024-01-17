from blog.form import RegstrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, get_flashed_messages
from blog.models import User, Post
from blog import app, db, bcrypt
from flask_login import login_user, current_user
@app.route('/')
def home():
    message = get_flashed_messages(with_categories=True)
    return render_template("home.html", message=message)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_auithenticated():
        return redirect(url_for('home'))
    form = RegstrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit() 
        flash("Your account has been created you can log in!", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        return redirect(url_for('home'))
    if form.is_submitted():
        flash('Login unsuccessful. Please check your email and password.', 'error')
    return render_template("login.html", title="Login", form=form)