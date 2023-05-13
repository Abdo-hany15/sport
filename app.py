import os
import sqlalchemy
from flask import Flask, session
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from database import db
from sqlalchemy_utils import database_exists, create_database


def make_app(configclass=Config):
    app = Flask(__name__)
    # why from object "you mean that configclass is a object"
    app.config.from_object(configclass)
    app.app_context().push()  # i dont understand what this doing

    # check of database is exists
    if not database_exists(app.config.get("SQLALCHEMY_DATABASE_URI")):
        create_database(app.config.get("SQLALCHEMY_DATABASE_URI"))

    # Initialize Flask extensions here
    # we change db=SQLALchemy(app)
    db.init_app(app)

    Config
    CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    Migrate(app, db, compare_type=True)

    with app.app_context():

        from club.model import Club
        from player.model import Player

        # Import a module / component using its blueprint handler variable
        from club.view import cl as club_view
        from player.view import pl as player_view

        # Register blueprint(s)
        app.register_blueprint(club_view)
        app.register_blueprint(player_view)

        # Sample HTTP error handling

        @app.errorhandler(404)
        def not_found(error):
            return str(404)

        @app.route('/favicon.ico')
        def favicon():
            return "work"

        @app.route('/')
        def test_page():
            return '<h1>Testing the Flask Application Factory Pattern</h1>'

        db.create_all()
        # db.session.commit()

    return app


if __name__ == ("__main__"):
    app = make_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
