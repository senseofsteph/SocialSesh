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
def show_homepage():
    """Display homepage with one button to create profile and another button to log in."""

    return render_template("index.html")


@app.route("/form")
def show_create_profile_form():
    """Display form to create a new profile account."""
    
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def create_user_profile():
    """Create a new profile account."""

    #TODO verify is password length and email are accurate

    firstname = request.form['fname']
    lastname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']

    #TODO add user to db
    user = crud.create_user(fname=firstname,lname=lastname, email=email, password=password, phone=phone)
    
    #TODO verify if the user is in the db.
    # if not add user to db 


    session['user'] = user
    
    return redirect("/login")


@app.route("/login")
def show_login():
    """Display page for user to login to."""

    if "user_id" in session and session["user_id"]:
        session_id = session["user_id"]
        return redirect("/profile")
    else: 
        return render_template("login.html")


@app.route("/login", methods=["POST"]) 
def login_user():
    """Log user into profile."""

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email_and_password(email, password)

    if not user:
        flash("Invalid email and/or password")
    else:
        session['user_id'] = user.user_id
        flash("Welcome, you're logged in")
        return redirect("/profile")

    
@app.route("/profile")
def dashboard():
    """Display user profile account page"""

     # if "user" in session:
    # TODO if the user key is in session then show logout 
    # TODO else show login prompt

    return render_template("profile.html")




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
