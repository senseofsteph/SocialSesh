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


@app.route("/profile")
def show_create_profile_form():
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
    
    #TODO verify if the user is in the db.
    # if not add user to db 

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
def show_login():
    """Display page for user to login to."""
    

    return render_template("login.html")


@app.route("/login", methods=["POST"]) 
def get_login():
    """Display page for user to login to."""

      # if "user" in session:
        # show their profile

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email_and_password(email, password)

    if not user:
        flash("Invalid email and/or password")
    else:
        session['user_id'] = user.user_id
        flash("Welcome, you're logged in")
        return redirect("/dashboard")

    
@app.route("/dashboard")
def dashboard():
    """Display user profile account page"""

     # if "user" in session:
    # TODO if the user key is in session then show logout 
    # TODO else show login prompt

    return render_template("dashboard.html")




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
