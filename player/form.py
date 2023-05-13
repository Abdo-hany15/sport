from flask_wtf import FlaskForm
# func my_custom_length
from wtforms import StringField, PasswordField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email, Length
# max in leangth doesnt gave u then the no you choose it


def my_custom_length(form, field):
    """ 
    a custom func insteade of Length
    """
    if len(field.data) < 2:
        raise ValidationError(message="Enter just two number\'abdo\' ")


class PlayerForm(FlaskForm):
 # NOTE player_name is a field
    player_name = StringField(label="playerName", validators=[
                              DataRequired(), my_custom_length])
    player_id = PasswordField(label="playerNaumber",
                              validators=[DataRequired()])
    # To show message of length go to player html
    email = EmailField(label="playerEmail", validators=[DataRequired(), Email(
        message="Please inter your email", granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
