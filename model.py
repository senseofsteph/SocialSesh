"""Models for social session app."""


from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime, date, time

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    
    def __init__(self, fname, lname, email, password, phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.phone = str(phone)

    # users_events = a list of User_Event objects

    def __repr__(self): 
        """Show info about user."""

        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email} phone={self.phone}>'


class Event(db.Model):
    """An event."""

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_type = db.Column(db.String,
                              db.ForeignKey('event_types.event_type'), 
                              nullable=False)
    event_name = db.Column(db.String, nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    event_start_time = db.Column(db.Time, nullable=False)
    # event_date = db.Column(db.DateTime, nullable=False)
    # event_start_time = db.Column(db.String, nullable=False)
    event_description = db.Column(db.Text, nullable=False)
    event_photo = db.Column(db.String, nullable=False)

    def __init__(self, event_type, event_name, event_date, event_start_time, event_description, event_photo):
        self.event_type = event_type
        self.event_name = event_name
        self.event_date = event_date
        self.event_start_time = event_start_time
        self.event_description = event_description
        self.event_photo = event_photo

    # users_events = a list of User_Event objects

    def __repr__(self):
        """Show info about the event."""

        return f'<Event event_id={self.event_id} event_type_id={self.event_type} event_name={self.event_name}>'


class User_Event(db.Model):
    """A user's list of events."""

    __tablename__ = 'users_events'

    users_events_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    event_id = db.Column(db.Integer, 
                         db.ForeignKey('events.event_id'),
                         nullable=False)

    user = db.relationship('User', backref='users_events')
    event = db.relationship('Event', backref='users_events')

    def __init__(self, user_id, event_id):
        self.user_id=user_id
        self.event_id=event_id
        
    
    def __repr__(self):
        """Show info about users created events."""

        return f'<User_Event users_events_id={self.user_events_id} user_id={self.user_id} event_id={self.event_id}>'



class Event_Type(db.Model):
    """A type of event category."""

    __tablename__ = 'event_types'

    event_type = db.Column(db.String, primary_key=True)
    event_type_description = db.Column(db.Text, nullable=False)
    
    def __init__(self, event_type, event_type_description):
        self.event_type = event_type
        self.event_type_description = event_type_description


    def __repr__(self):
        """Show info about event category type"""

        return f'<Event_Type event_type_id={self.event_type} event_type_name={self.event_type_description}>'


def connect_to_db(flask_app, db_uri='postgresql:///socialsesh', echo=True):
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

    db.create_all()

