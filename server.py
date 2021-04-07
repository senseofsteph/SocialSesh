"""Server for social sessions app."""


from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "socialsesh"
app.jinja_env.undefined = StrictUndefined




@app.route("/")
def index():
    """Show homepage with two buttons for the user to select, create profile or log in."""

    return render_template("index.html")


@app.route("/profile")
def profile():
    """Display form to create a profile account."""
    
    # if "user" in session:
        # show their profile

    return render_template("profile.html")


@app.route("/profile", methods=["POST"])
def create_profile():
    """Once form is submitted, reroute user to log-in page."""

    firstname = request.form['fname']
    lastname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']

    #TODO verify that the password is something sane email, etc. 

    ## if password is less than 7 letters
        ## flash message: password must be 7 letters

    ## if email is not an actual email
       ## flash message: 

    #TODO add user to db
    # user = crud.create_user(fname=firstname, lname= , email, password, phone)

    # # Login them in 
    # if user != null
    #     session["user"] = email
    
    # return redirect("/profile")


@app.route("/login") 
def login():
    """Display page for user to login to."""

    # if "user" in session:
    # TODO if the user key is in session then show logout 
    # TODO else show login promt 
    
    # user can log into account profile page

@app.route("/dashboard")
def dashboard():
    """Display user profile account page"""

    # flash message to user: you are logged in!




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
