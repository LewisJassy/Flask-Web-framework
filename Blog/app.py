from flask import Flask, render_template, url_for, flash, redirect
from form import RegstrationForm, LoginForm
from flask_bootstrap import Bootstrap5
app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = 'c6d75c5b3fe288fa1ced520a011e19'
posts = [{
    "author": 'Lewis Njaci',
    " title": "Blog post",
    "content": 'Blog'
},
    {
        "None",
    }
]

@app.route('/')
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegstrationForm()
    if form.validate_on_submit():
        flash("Registration successful!", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)