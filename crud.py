"""CRUD operations."""


from model import db, User, Event, User_Event, Event_Type, connect_to_db





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
