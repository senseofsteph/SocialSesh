"""Server for social sessions app."""


from flask import (Flask, render_template, request, flash, session, redirect)
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
    """Display homepage with one button to create profile and another button to log in."""

    return render_template("index.html")


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

    user = crud.create_user(fname=firstname, lname=lastname, email=email, password=password, phone=phone)

    # if crud.is_new_user(fname, lname, email, password, phone): 
    #     flash('Invalid entry. Please fill out entire form to create an account')
    #     return redirect("/form")
        
    # else:
    #     user = crud.is_new_user(db.session.add(User(fname=fname, lname=lname, email=email, password=password, phone=phone)))
    #     db.session.commit()
    #     flash('Account created! Please log in')
        
    # return redirect("/login")

    if user:
        crud.create_user(firstname,lastname,email,password,phone)
        flash('Account created! Please log in')
    else:
        flash('Invalid entry. Please fill out entire form to create an account')
        return redirect("/form")
    
    return redirect("/login")


@app.route("/login")
def show_login():
    """Display form for user to login to."""
 
    return render_template("login.html")


@app.route("/login", methods=["POST"]) 
def login_user():
    """Log user into profile account."""

    # add a name variable to great user on profile
    email = request.form.get('email')
    password = request.form.get('password')

    # if login credentials valid, log in user by updating
    if crud.is_email_and_password_valid(email, password):
        # session['user_id'] and setting it to email
        session['user_id'] = email
        flash("You're logged in.")
        return redirect("/profile")
    else:
        flash("Invalid email and/or password")
        return redirect("/login")


@app.route("/profile")
def show_profile():
    """Display user profile page."""

     # TODO: find a way to get user name so hello is personalized

    return render_template("profile.html")


@app.route("/calendar")
def calendar():
    """Display calendar of scheduled virtual events"""

    return render_template("calendar.html")


@app.route("/category")
def select_event_category():
    """Display form for user to select event category"""

    return render_template("category_events.html")


@app.route("/api/category", methods=["POST"])
def get_event_by_category():
    """Get event category selection"""

    selected_event_type = request.form.get('types')

    # return redirect("/category/" + selected_event_type)

    # create events dict and iterate through events object list 
    # for event in events:
    # events_dict = {
    # event_name: {
        # "event_type": event["event_type"],
        # "event_name": event["event_name"],
        # "event_date": "2021-05-08",
        # "event_start_time": "7:00",
        # "event_description": "Full access to The Weeknd on tour-After Hours World Tour",
        # "event_photo": "/static/img/concert-768722_1280.jpg"
    #   }
    # }
    
    template = ""

    events = crud.get_event_by_type(selected_event_type.title())
    print(events)

    if selected_event_type == "activity":
        template = "type_activity.html"
    elif selected_event_type == "celebration":
        template = "type_celebration.html"
    elif selected_event_type == "educational":
        template = "type_educational.html"
    elif selected_event_type == "entertainment":
        template = "type_entertainment.html"


    test_dict = {}

    for event in events:
        test_dict[event.event_name] = {
            'event_name': event.event_name,
            'event_description': event.event_description
        }
        
    return test_dict
    # return render_template(template, events=events)
    # return (events, )
  

# @app.route("/category/<event_type>")
# def show_categories(event_type):
#     """Display all events under selected category"""

#     template = ""

#     events = crud.get_event_by_type(event_type.title())

#     if event_type == "activity":
#         template = "type_activity.html"
#     elif event_type == "celebration":
#         template = "type_celebration.html"
#     elif event_type == "educational":
#         template = "type_educational.html"
#     elif event_type == "entertainment":
#         template = "type_entertainment.html"
    
#     return render_template(template, events=events)


# @app.route("/category/<event_type>", methods=["GET"])
# def show_event_in_category(event_id):

#     event = crud.get_event_by_id(event_id)

#     return redirect("/events/<event_id>", event=event)   


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


@app.route("/events/<event_type>", methods=["GET"])
def get_registration():
    """Register for event."""

    return redirect("/register")


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

    flash("You've been logged out. See you soon!")

    return redirect("/")




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
