"""Server for social sessions app."""


from flask import Flask 
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "my_first_project"
app.jinja_env.undefined = StrictUndefined




@app.route('/')
def homepage():
    """Display homepage."""

    return render_template('index.html')


@app.route('/','/login')
def login():
    """User can log into profile."""

    # user will log in with their Google account using OATH


@app.route('/profile')
def profile():
    """Display user profile page"""

    # user can see profile page details


@app.route('/activity')
def select_activity():
    """User can select one activity to do."""

    # user will select an activity by click or scroll bar


@app.route('/result')
def local_users():
    """Display map and four local users that are ready to pair for the activity"""

    # display Google map with pinpoint location of the other local users
    # user will select one local user to schedule the social session activity



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
