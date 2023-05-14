from flask_wtf import FlaskForm
# func my_custom_length
from wtforms import StringField, ValidationError, FloatField
from wtforms.validators import DataRequired
# max in leangth doesnt gave u then the no you choose it


# def my_custom_length(form, field):
#     """
#     a custom func insteade of Length
#     """
#     if len(field.data) < 2:
#         raise ValidationError(message="Enter just two number\'abdo\' ")


class PlayerForm(FlaskForm):
    player_name = StringField(label="PlayerName", validators=[DataRequired()])
    salary = FloatField(label="Salary")
