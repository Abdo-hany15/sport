from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class ClubForm(FlaskForm):
    name = StringField(label="PlayerName")
    code = PasswordField(label="Password")
