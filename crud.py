"""CRUD operations."""


from model import db, User, Activity, User_Activity, connect_to_db





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
     