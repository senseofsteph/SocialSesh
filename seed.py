"""Script to seed database."""


import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server 

os.system('dropdb socialsesh')
os.system('createdb socialsesh')

model.connect_to_db(server.app)
model.db.create_all()

# Load event data from JSON file
with open('data/events.json') as e:
  event_data = json.loads(e.read())

# Create events, store them in a list so we can use them 
# to create artificial events and searches
events_in_db = []
for event in event_data:
    event_name, event_duration, event_description, event_location = (event['event_name'],
                   event['event_duration'],
                   event['event_description'],
                   event['event_location'])
    event_date = datetime.strptime(event['event_date'],'%Y-%m-%d')
    event_start_time = datetime.strptime(event['event_start_time'], '%H:%M')

    db_event = crud.create_event(event_name, event_date, event_start_time, event_duration, event_description, event_location)

    events_in_db.append(db_event)

# create fake users 10 using python faker library, call crud functions in to seed into database

 




  