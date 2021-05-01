"""Models for social session app."""


from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime, date, time
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


#**** -------- User Models --------- ****#

#**** ------------------------------- ****#


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True, index=True)
    # password = db.Column(db.String(100))
    password_hash = db.Column(db.String(100))
    phone = db.Column(db.String, nullable=False)

    # users_events = a list of User_Event objects
    
    def set_password(self, password):
        """Creates hash of password"""

        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        """Confirms if password is hashed"""

        return check_password_hash(self.password_hash, password)
    

    def __init__(self, fname, lname, email, password, phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.set_password(password)
        self.phone = str(phone)

    def __repr__(self): 
        """Show info about user."""

        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email} phone={self.phone}>'


#**** -------- Event Model --------- ****#

#**** ------------------------------- ****#


class Event(db.Model):
    """An event."""

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_type = db.Column(db.String(50),nullable=False)
    event_name = db.Column(db.String(100), nullable=False)
    event_start_date = db.Column(db.DateTime, nullable=False)
    event_end_date = db.Column(db.DateTime, nullable=False)
    event_description = db.Column(db.Text, nullable=False)
    event_photo = db.Column(db.String, nullable=False)

    # users_events = a list of User_Event objects


    def __init__(self, event_type, event_name, event_start_date, event_end_date, event_description, event_photo):
        self.event_type = event_type
        self.event_name = event_name
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.event_description = event_description
        self.event_photo = event_photo

    def __repr__(self):
        """Show info about the event."""

        return f'<Event event_id={self.event_id} event_type={self.event_type} event_name={self.event_name}>'


#**** ------ User_Event Model ------- ****#

#**** ------------------------------- ****#


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
        """Show info about events created by users."""

        return f'<User_Event users_events_id={self.user_events_id} user_id={self.user_id} event_id={self.event_id}>'


#**** ----- Connect to Database ----- ****#

#**** ------------------------------- ****#


def connect_to_db(flask_app, db_uri='postgresql:///socialsesh', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = False
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


#**** ------------------------------- ****#

#**** ------------------------------- ****#


if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)
    db.create_all()


