"""Models for social session app."""


from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)
    phone = db.Column(db.String)
    user_photo = db.Column(db.String)
    user_bio = db.Column(db.Text)
    user_zipcode = db.Column(db.Integer)

    def __repr__(self):
        """Show info about user."""

        return f'<User user_id={self.user_id} firstname={self.fname} lastname={self.lname} email={self.email} phone={self.phone}>'

    
class Event(db.Model):
    """An event."""

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_type_id = db.Column(db.Integer) # a foreign key?
    event_name = db.Column(db.String)
    event_date = db.Column(db.DateTime)
    event_start_time = db.Column(db.String)
    event_duration = db.Column(db.Integer)
    event_description = db.Column(db.Text)
    event_location = db.Column(db.String)
    event_zipcode = db.Column(db.Integer)
    event_photo = db.Column(db.String)

    def __repr__(self):
        """Show info about the event."""

        return f'<Event event_id={self.event_id} event_type_id={self.event_type_id} event_name={self.event_name} event_date={self.event_date}>'


class User_Event(db.Model):
    """A user's list of events."""

    __tablename__ = 'users_events'

    users_events_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)

    def __repr__(self):
        """Show info about users created events."""

        return f'<User_Event users_events_id={self.user_events_id} user_id={self.user_id} event_id={self.event_id}>'



class Event_Type(db.Model):
    """A type of event category."""

    __tablename__ = 'event_types'

    event_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_type_name = db.Column(db.String)
    event_type_description = db.Column(db.Text)

    def __repr__(self):
        """Show info about event category type"""

        return f'<Event_Type event_type_id={self.event_type_id} event_type_name={self.event_type_name} event_type_description={self.event_type_description}>'



def connect_to_db(flask_app, db_uri='postgresql:///users_events', echo=True):
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
