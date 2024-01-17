from flask import Flask

from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = 'c6d75c5b3fe288fa1ced520a011e19'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = "login"

from blog import routes