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
    """Create a new user profile."""

    #TODO verify is password length and email are accurate

    firstname = request.form['fname']
    lastname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']

    user = crud.create_user(fname=firstname, lname=lastname, email=email, password=password, phone=phone)

    if user:
        crud.create_user(firstname,lastname,email,password,phone)
        flash('Account created! Please log in')
    else:
        flash('Invalid. Please try again or create an account')
        return redirect("/form")
    
    return redirect("/login")


@app.route("/login")
def show_login():
    """Display page for user to login to."""
 
    return render_template("login.html")


@app.route("/login", methods=["POST"]) 
def login_user():
    """Log user into profile."""

    email = request.form['email']
    password = request.form['password']

    registered = crud.validate_user_email_and_password(email, password)

    if registered:
        session['user_id'] = email
        flash("You're logged in.")
        return redirect("/profile")

    else:
        flash("Invalid email and/or password")
        return redirect("/login")


@app.route("/profile")
def show_profile():
    """Display user profile page."""

     # if "user" in session:
    # TODO if the user key is in session then show logout 
    # TODO else show login prompt
    # TODO add user name at hello using jinja

    return render_template("profile.html")


@app.route("/profile", methods=["POST"])
def get_event_type():
    """Display different event types for user to select."""

    return redirect("/events")


@app.route("/events")
def show_event():
    """View all events."""

    events = crud.get_events()

    return render_template("all_events.html",events=events)


@app.route("/events", methods=["POST"])
def get_event():
    """View details about specific event."""

    # TODO show the exact event

    # TODO 

    #return render_template("event_details.html", event=event)


@app.route("/events/<event_type>")
def show_event_type(event_type):
    """Show details of event in particular category."""

    # TODO show the selected event type and event
    # TODO add crud function

    # if user select activity:
        # show all db event under activity

    event = crud.get_event_type(event_type)

    return render_template("event_details.html", event=event)






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
