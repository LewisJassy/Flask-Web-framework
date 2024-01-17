from flask import Flask

from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = 'c6d75c5b3fe288fa1ced520a011e19'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from blog import routes