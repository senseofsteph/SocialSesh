"""Script to seed database."""


import os
import json
from random import choice, randint
from datetime import datetime, date, time

import crud
import model
import server 

os.system('dropdb socialsesh')
os.system('createdb socialsesh')

model.connect_to_db(server.app)
model.db.create_all()


# Load users data from JSON file
with open('data/users.json') as u:
  users_data = json.loads(u.read())

  for user in users_data:

    fname = user['fname']
    lname = user['lname']
    email = user['email']
    password = user['password']
    phone = user['phone']

  crud.create_user(fname, lname, email, password, phone)
    

# Load events data from JSON file
with open('data/events.json') as e:
  events_data = json.loads(e.read())

  for event in events_data:
    
    event_type = event['event_type']
    event_name  = event['event_name']
    event_date = datetime.strptime(event['event_date'],'%Y-%m-%d')
    event_start_time = datetime.strptime(event['event_start_time'], '%H:%M')
    event_description = event['event_description']
    event_photo = event['event_photo']
    
  crud.create_event(event_type, event_name, event_date, event_start_time, event_description, event_photo)




 




  