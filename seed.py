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


# Load event types data from JSON file
with open('data/event_types.json') as e:
  event_types_data = json.loads(e.read())

for types in event_types_data:

    event_type = types['event_type']
    event_type_description = types['event_type_description']

    crud.create_event_type(event_type, event_type_description)
    

# Load events data from JSON file
with open('data/events.json') as f:
  events_data = json.loads(f.read())

for event in events_data:
    
    event_name  = event['event_name']
    event_description = event['event_description']
    event_date = datetime.strptime(event['event_date'],'%Y-%m-%d')
    event_start_time = datetime.strptime(event['event_start_time'], '%H:%M')
    event_photo = event["event_photo"]
    event_type = event["event_type"]

    crud.create_event(event_type, event_name, event_date, event_start_time, event_description, event_photo)

    



 




  