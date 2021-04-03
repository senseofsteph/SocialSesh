"""Script to seed database."""


import os
import json
from random import choice, randint

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
# to create artificial searches
events_in_db = []
for event in event_data:
    event_name, event_date, event_start_time, event_duration, event_description, event_location, event_photo = (event['event_name'],
                                   event['event_date'],
                                   event['event_start_time'],
                                   event['event_duration']),
                                   event['event_description'],
                                   event['event_location'],
                                   event['event_photo']
    event_date = datetime.strptime(event['event_date'], '%Y-%d-%m')

    db_movie = crud.create_event(event_name, 
                                 event_date, event_start_time, event_duration, event_description, event_location, event_photo)

    events_in_db.append(db_event)


# Nice to have feature?
# Create 10 users; each user will be able to create and search for events
for n in range(10):
  email = f'user{n}@test.com' # Voila! A unique email!
  password = 'test'

  user = crud.create_user(email,password)

  return user




  