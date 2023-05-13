from database import db


class Club(db.Model):
    """
    argument of relationship must be capital like class name
    backref can be small because of the model
    laze prefare to be T
    in relations
    one :make db.relation and add column name s like courses
    many: make or put Foreign key on it and name single _id
    db.ForeignKey("")can be small like ("instructor_time.id")

    """
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(65), unique=False, nullable=False)
    league_division = db.Column(db.String(1), unique=False, nullable=False)
    players = db.relationship("Player", backref="player", lazy=True)
