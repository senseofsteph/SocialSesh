"""Models for social session app."""


from flask_sqlalchemy import SQLAlchemy 

db = SQAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'


class Interest(db.Model):
    """An interest."""

    __tablename__ = 'interests'


class User_Activity(db.Model):
    """A user's interest."""

    __tablename__ = 'user_interest'


def connect_to_db(flask_app, db_uri='postgresql:///user_interest', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = False
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

    # db.create_all()
