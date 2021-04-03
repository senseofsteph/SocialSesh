"""Models for social session app."""


from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String, nullable=False)
    user_photo = db.Column(db.String, nullable=False)
    user_bio = db.Column(db.Text, nullable=False)
    

    # users_events = a list of User_Event objects

    def __repr__(self): 
        """Show info about user."""

        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email} phone={self.phone}>'

    
class Event(db.Model):
    """An event."""

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_type_id = db.Column(db.Integer,
                              db.ForeignKey('event_types.event_type_id'), 
                              nullable=False)
    event_name = db.Column(db.String, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    event_start_time = db.Column(db.String, nullable=False)
    event_duration = db.Column(db.Integer, nullable=False)
    event_description = db.Column(db.Text, nullable=False)
    event_location = db.Column(db.String, nullable=False)
    event_photo = db.Column(db.String, nullable=False)

    # users_events = a list of User_Event objects

    def __repr__(self):
        """Show info about the event."""

        return f'<Event event_id={self.event_id} event_type_id={self.event_type_id} event_name={self.event_name}>'


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

    def __repr__(self):
        """Show info about users created events."""

        return f'<User_Event users_events_id={self.user_events_id} user_id={self.user_id} event_id={self.event_id}>'



class Event_Type(db.Model):
    """A type of event category."""

    __tablename__ = 'event_types'

    event_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_type_name = db.Column(db.String, nullable=False)
    event_type_description = db.Column(db.Text, nullable=False)
    

    def __repr__(self):
        """Show info about event category type"""

        return f'<Event_Type event_type_id={self.event_type_id} event_type_name={self.event_type_name}>'



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
