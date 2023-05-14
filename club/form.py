from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class ClubForm(FlaskForm):
    name = StringField(label="clubname")
    league_division = PasswordField(label="Password")
