"""Server for social sessions app."""


from flask import (Flask, render_template, request, flash, session, redirect)
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

import send_sms
from model import connect_to_db
import crud 
import os

from jinja2 import StrictUndefined


os.system('source secrets.sh')

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
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
        flash('Invalid. Please fill out entire form to create an account')
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

    return render_template("profile.html")


@app.route("/profile", methods=["POST"])
def get_event_type():
    """Display different event types for user to select."""

    return redirect("/events")


@app.route("/events")
def all_events():
    """View all events."""

    events = crud.get_events()

    return render_template("all_events.html",events=events)


@app.route("/events/<event_id>")
def show_event(event_id):
    """Show details on a particular event."""

    event = crud.get_event_by_id(event_id)

    return render_template("event_details.html", event=event)


@app.route("/events/<event_type>", methods=["POST"])
def get_registration():
    """Register for event."""

    return redirect("/register")


@app.route("/register")
def show_registration():
    """Display form to register for event."""

    return render_template("register.html")


@app.route("/register", methods=["POST"])
def registration():
    """Display form to register for event."""

    phone = request.form['phone']

    confirmed = send_sms.send_sms_to(phone)

    if confirmed:
        send_sms.send_sms_to(phone)
        flash("Phone number verified")
        return redirect("/confirmation")

    else:
        flash("Invalid phone number. Please try again")
        return redirect("/register")


@app.route("/confirmation")
def confirmation():
    """Display confirmation of event registration."""

    return render_template("thanks.html")


@app.route("/confirmation", methods=["POST"])
def send_confirmation():
    """Send SMS text message confirmation of event registration."""

    return redirect("/confirmation")


# @app.route("/confirmation", methods=["POST"])
# def sms_reply():
#     """Send SMS text message response to user."""

#     resp = MessagingResponse()
#     resp.message("You're welcome. Feel free to Reach out to SocialSesh for any questions and/or feedback")

#     return str(resp)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
