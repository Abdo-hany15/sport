from flask import Blueprint, render_template
from player.form import PlayerForm
from player.model import Player
from database import db
pl = Blueprint('player', __name__, url_prefix='/sign')


@pl.route('/', methods=['GET', 'POST'])
def player_sign():
    form = PlayerForm()
    if form.validate_on_submit():
        nname = form.player_name.data
        salary = form.salary.data
        # the data to be inserted into player model - the table, player
        # nname is guest a variable i created to recive data of player name "name"->column in player(db.model)
        player = Player(name=nname, salary=salary)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(player)
        db.session.commit()
        return "Data saved to database"
    return render_template('player.html', form=form)


# @pl.route('/confirm', methods=['GET', 'POST'])
# def club_confirm():
#     form = PlayerForm(request.form)
#     print(form)
#     if request.method == 'POST' and form.validate():
#         data = Player(form.player_name.data,
#                       form.player_id.data, form.salary.data)
#         db.session.add(data)
#         db.session.commit()
#         flash("Your data has been saved")
#     return render_template('player.html', form=form)
