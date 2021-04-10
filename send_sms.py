"""Function to send Twilio SMS text message."""

import os
import re
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_sms_to(phone='+12099147702'):
  
  number = re.search(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', phone)
  print(type(number.group(0)))

  # check the lenght of string
  # check the 1st two chars of string 
  # if its 12 = valid

  if phone != None:
    message = client.messages \
      .create(
        body='Thank you for registering your social session. Be safe and enjoy your virtual event!',
        from_='+16282004021',
        to=phone 
      )







