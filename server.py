"""Server for social sessions app."""


from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "socialsesh"
app.jinja_env.undefined = StrictUndefined

# route functions for each webpage

@app.route("/")
def index():
    """Show homepage with two buttons for the user to select, create profile or log in."""



    return render_template("index.html")


@app.route("/profile", methods=["POST"])
def profile():
    """User can create a profile account."""

    # user will create profile with full name, email, password and phone number
    return render_template("profile.html")


@app.route("/login") 
def login():
    """Display page for user to login to."""

    # user can log into account profile page






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
