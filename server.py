"""Script to run server for virtual events app."""


from flask import (Flask, flash, jsonify, render_template, request, redirect, session)
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

import send_sms
from model import connect_to_db
import crud 
import os

from jinja2 import StrictUndefined

os.system("source secrets.sh")

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def show_homepage():
    """Display homepage."""

    return render_template("index.html")


#**** ---- Create Profile Routes ---- ****#

#**** ------------------------------- ****#


@app.route("/form")
def show_create_profile_form():
    """Display form to create a new profile account."""
    
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def create_user_profile():
    """Create a new user profile."""

    firstname = request.form.get('fname')
    lastname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    phone = request.form.get('phone')
    # image = request.form.get('image')

    # add default image to users json file
    # eventually give user an option to upload their own photo
    # style profile page to diplay default image unless user uploads their own image
    # add section for bio or user profile account
    
    
    user = crud.create_user(fname=firstname, lname=lastname, email=email, password=password, phone=phone)

    # user = crud.create_user(fname=firstname, lname=lastname, email=email, password=password, phone=phone, image=image)

    if user:
        crud.create_user(firstname,lastname,email,password,phone)
        # crud.create_user(firstname,lastname,email,password,phone,image)
        flash("Account created! Please log in")
    else:
        flash("Invalid entry. Please fill out entire form")
        return redirect("/form")
    
    return redirect("/login")


#**** -------- Log-in Routes -------- ****#

#**** ------------------------------- ****#


@app.route("/login")
def show_login():
    """Display form for user to login."""
 
    return render_template("login.html")


@app.route("/login", methods=["POST"]) 
def login_user():
    """Log user into profile account."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
   
    if crud.is_email_and_password_valid(email, password):

        session['user_id'] = email
        session['user_name'] = user.fname
        flash(f"Welcome {user.fname}, you're logged in!")
        return redirect("/profile")
    else:
        flash("Invalid email and/or password")
        return redirect("/login")


#**** ---- Profile Account Route ---- ****#

#**** ------------------------------- ****#


@app.route("/profile")
def show_profile():
    """Display user profile page."""

    return render_template("profile.html")


#**** -- Events on Calendar Routes -- ****#

#**** ------------------------------- ****#


@app.route("/calendar")
def calendar():
    """Display calendar of scheduled virtual events"""

    return render_template("calendar.html")


@app.route("/api/calendar")
def show_events_on_calendar():
    """Display all scheduled events on full calendar"""

    events = crud.get_events()
    
    calendar = {
        "initialView": "dayGridMonth",
        "initialDate": "2021-05-01", 
        "headerToolbar": {
                "left": "prev,next today",
                "center": "title",
                "right": "dayGridMonth,timeGridWeek,timeGridDay"
            },
        "events":[]
    }

    for event in events:
        calendar['events'].append({
            "title": event.event_name,
            "start": event.event_start_date.isoformat(),
            "end": event.event_end_date.isoformat()
            })

    return jsonify(calendar)     


#**** -- Events by Category Routes -- ****#

#**** ------------------------------- ****#


@app.route("/category")
def select_event_category():
    """Display form for user to select event category"""

    return render_template("category_events.html")


@app.route("/api/category", methods=["POST"])
def get_event_by_category():
    """Return information about event category"""

    selected_event_type = request.form.get('types')

    events = crud.get_event_by_type(selected_event_type.title())
    
    category_list = []

    for event in events:
        category_list.append({
            "event_id": event.event_id,
            "event_name": event.event_name,
            "event_start_date": event.event_start_date.isoformat(),
            "event_end_date": event.event_end_date.isoformat(),
            "event_description": event.event_description,
            "event_photo": event.event_photo
            })

    return jsonify(category_list)


#**** ------ All Events Routes ------ ****#

#**** ------------------------------- ****#


@app.route("/events")
def all_events():
    """View all events."""

    events = crud.get_events()

    return render_template("all_events.html",events=events)


@app.route("/events/<event_id>")
def show_event(event_id):
    """Show details on a particular event."""

    event = crud.get_event_by_id(event_id)
    
    event_start_date = event.event_start_date.strftime('%a %b-%d-%Y %I:%M %p')
    event_end_date = event.event_end_date.strftime('%a %b-%d-%Y %I:%M %p')

    return render_template("event_details.html", event=event, event_start_date=event_start_date, event_end_date=event_end_date)


@app.route("/events/<event_type>", methods=["GET"])
def get_registration():
    """Register for event."""

    return redirect("/register")


#**** -- Event Registration Routes -- ****#

#**** ------------------------------- ****#


@app.route("/register")
def show_registration():
    """Display form to register for event."""

    return render_template("register.html")


@app.route("/register", methods=["POST"])
def registration():
    """Validates user phone number to register for event."""

    phone = request.form.get('phone')

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


@app.route("/confirmation", methods=["GET"])
def send_confirmation():
    """Display redirect options to user."""

    return redirect("/confirmation")


@app.route("/logout")
def logout():
    """Log user out of profile account."""

    session.pop('user_id', None) 
    session.pop('user_name', None) 

    flash("You've been logged out. See you soon!") 

    return redirect("/")


#**** ------------------------------- ****#

#**** ------------------------------- ****#


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
