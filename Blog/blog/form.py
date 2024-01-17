from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User

class RegstrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email Address", validators=[DataRequired(), Length(min=2, max=20), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Pasword", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken please choose a different name")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken please choose a different name")
class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Length(min=2), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Pasword", validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Sign In")