"""Script to run CRUD (create, read, update, delete) operations."""


from model import db, User, Event, User_Event, connect_to_db
from datetime import datetime, date, time


#**** --------- User queries -------- ****#

#**** ------------------------------- ****#


def create_user(fname, lname, email, password, phone, image):
    """Create and return a new user."""

    user = User.query.filter(User.email == email).first()

    if user == None:

        user = User(fname=fname, lname=lname,
                   email=email, password=password,
                   phone=phone, image=image)
        db.session.add(user)
        db.session.commit()
        return True
        
    else:
        return False

    
def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_fname(fname):
    """Return a user by first name."""

    return User.query.filter(User.fname)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def is_email_and_password_valid(email, password):
    """Return True if email and password are valid."""

    user = User.query.filter(User.email == email).first()
   
    if user:

        return user.check_password(password)

    return user is not None

   
#**** -------- Event queries -------- ****#

#**** ------------------------------- ****#


def create_event(event_type, event_name, event_start_date, event_end_date, event_description, event_photo):
    """Create and return a new event."""

    event = Event.query.filter(Event.event_type == event_type,
                               Event.event_name == event_name, 
                               Event.event_start_date == event_start_date, 
                               Event.event_end_date == event_end_date, 
                               Event.event_description == event_description, 
                               Event.event_photo == event_photo).first()

    if event == None:
        db.session.add(Event(event_type=event_type, event_name=event_name, 
                             event_start_date=event_start_date, 
                             event_end_date=event_end_date,
                             event_description=event_description, 
                             event_photo=event_photo))
        db.session.commit()
        return True
    else:
        return False


def get_events():
    """Return all events."""

    return Event.query.all()


def get_event_by_id(event_id):
    """Return an event by primary key."""

    return Event.query.get(event_id)


def get_event_by_type(event_type):
    """Return an event by event type."""

    return Event.query.filter(Event.event_type == event_type).all()


def get_event_by_user(users_events_id):
    """Return all the users events by id."""

    return User_Event.query.get(users_events_id)


#**** ------------------------------- ****#

#**** ------------------------------- ****#


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
