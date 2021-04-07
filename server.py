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
    """Display homepage with one button to create profile and another button to log in."""

    return render_template("index.html")


@app.route("/profile")
def profile():
    """Display form to create a new profile account."""
    
    # if "user" in session:
        # show their profile


    return render_template("profile.html")


@app.route("/profile", methods=["POST"])
def create_profile():
    """Create a new profile account."""

    firstname = request.form['fname']
    lastname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    
    #TODO verify that the password is something sane email, etc. 

    if len(password) < 7 or len(password) > 12:
        return flash("Password should be at least 7 characters and less than 12 characters")

    

    #TODO add user to db
    user = crud.create_user(fname=firstname,lname=lastname, email=email, password=password, phone=phone)

    session['user'] = user

    # # Login them in 
    # if user != null
    #     session["user"] = email
    
    return redirect("/login")


@app.route("/login") 
def login():
    """Display page for user to login to."""


    # if "user" in session:
    # TODO if the user key is in session then show logout 
    # TODO else show login promt 
    
    # user can log into account profile page

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    """Display user profile account page"""

    # flash message to user: you are logged in!




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
