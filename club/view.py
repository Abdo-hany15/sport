from flask import Blueprint, render_template
from club.form import ClubForm

cl = Blueprint('club', __name__, url_prefix='/enroll')


@cl.route("/", methods=['GET', 'POST'])
def club_enroll():
    form = ClubForm()
    if form.validate_on_submit():
        return f"name:\' {form.name.data} \' code:\' {form.code.data} \'"
    return render_template("club.html", form=form)


@cl.route("/add")
def club_sssdd():

    return render_template("club.html")
