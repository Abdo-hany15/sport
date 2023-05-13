from flask import Blueprint, render_template
from player.form import PlayerForm

pl = Blueprint('player', __name__, url_prefix='/sign')


@pl.route('/', methods=['GET', 'POST'])
def player_sign():
    form = PlayerForm()
    if form.validate_on_submit():
        return f" player name is : {form.player_name.data} and his T-shert {form.player_id.data} and his email is {form.email.data}"
    return render_template('player.html', form=form)


@pl.route('/confirm')
def club_confirm():

    return render_template('player.html')
