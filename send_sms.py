"""Script to send Twilio SMS text message."""

import os
import re
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_sms_to(phone ='+12099147702'):
  
  number = re.search(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', phone)
  print(type(number.group(0)))

  # for phone nums that are not hard coded
  # need to confirm if it's an actual phone num
  # check the length of string 
  # should be at least 10 or up to 12 chars
  # check 1st two chars of string, should be: +1
  
  if phone != None:
    message = client.messages \
      .create(
        body ='Thank you for registering your social session. Be sure to save the date and time!',
        from_ ='+16282004021',
        to = phone 
      )
  return phone







