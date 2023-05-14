from flask import Blueprint, render_template, request
from club.form import ClubForm
from club.model import Club
from database import db
cl = Blueprint('club', __name__, url_prefix='/enroll')

# This route with using "wtform"


@cl.route("/", methods=['GET', 'POST'])
def club_enroll():
    form = ClubForm()
    if form.validate_on_submit():
        name = form.name.data
        league_division = form.league_division.data
        club = Club(name=name, league_division=league_division)
        db.session.add(club)
        db.session.commit()
        return 'Data saved to database'
        # return f"name:\' {form.name.data} \' code:\' {form.league_division.data} \'"
    return render_template("club.html", form=form)


# This route with using "request"
""" 
there was a problem ' jinja2.exceptions.UndefinedError: 'form' is undefined ' 
"""


@cl.route("/add", methods=['GET', 'POST'])
def club_sssdd():

    if request.method == 'POST':
        name = request.form['name']
        league_division = request.form.get('league_division')
        club = Club(name=name, league_division=league_division)
        db.session.add(club)
        db.session.commit()
        return 'Data saved to database'

    return render_template("club.html")
