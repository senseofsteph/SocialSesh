"""Server for social sessions app."""


from flask import Flask 
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "my_first_project"
app.jinja_env.undefined = StrictUndefined

# route functions for each webpage

@app.route('/')
def homepage():
    """Display homepage."""

    return render_template('index.html')


@app.route('/')
def login():
    """User can log into profile."""

    # user will log in with their email and password
    # or can create an account


@app.route('/profile/<user_id>') 
def profile():
    """Display user profile page"""

    # user can see profile page


@app.route('/')
def pick_interest():
    """User can select an interest."""

    # user will select an interest to comment on


@app.route('/sendmessage')
def send_message():
    """User can comment of specified interest."""

    # user can send a comment or feedback on interest
    # text, photo, resourceful link



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
