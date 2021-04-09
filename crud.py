"""CRUD (create, read, update, delete) operations."""


from model import db, User, Event, User_Event, Event_Type, connect_to_db
from datetime import datetime


def create_user(fname, lname, email, password, phone):
    """Create and return a new user."""

    # Check if the email is already being used
    user = User.query.filter(User.email == email).first()

    # If not, add the user
    if user == None:

        db.session.add(User(fname=fname, lname=lname, email=email, password=password, phone=phone))
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


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def validate_user_email_and_password(email, password):
    """Return a user by email and password."""

    user = User.query.filter(User.email == email, User.password == password).first()

    # if user != None:
    # if user.email and user.password:
    if user.fname:
        return True
    else:
        return False
    

def create_event(event_type, event_name, event_date, event_start_time, event_description, event_photo):
    """Create and return a new event."""

    event = Event(event_type=event_type,event_name=event_name, event_date=event_date, event_start_time=event_start_time, event_description=event_description, event_photo=event_photo)

    db.session.add(event)
    db.session.commit()

    return event


def get_events():
    """Return all events."""

    return Event.query.all()


def get_event_by_id(event_id):
    """Return an event by primary key."""

    return Event.query.get(event_id)


def get_event_by_user(users_events_id):
    """Return all the users events by id."""

    return User_Event.query.get(users_events_id)


def create_event_type(event_type, event_type_description):
    """Create an event type category."""

    event_type_name = Event_Type(event_type=event_type, event_type_description=event_type_description)

    db.session.add(event_type_name)
    db.session.commit()

    return event_type_name


def get_event_types():
    """Return all event types."""

    return Event_Type.query.all()


def get_event_type_by_id(event_type_id):
    """Return event type by id."""

    return Event_Type.query.get(event_type_id)


def get_event_by_type(event_type):
    """Return events under each event type."""

    return Event_Type.query.get(event_type)

  




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
