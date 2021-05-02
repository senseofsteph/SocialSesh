"""Script to send Twilio SMS text message."""


import os
import re
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


#**** ------ Send SMS Function ------ ****#

#**** ------------------------------- ****#


def send_sms_to(phone):
  
  # Regex to verify phone number
  number = re.search(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', phone)
  print(type(number.group(0)))

  if phone != None:
    message = client.messages \
      .create(
        body ='Thank you for registering your virtual social session. Be sure to save the date and time!',
        from_ ='+16282004021',
        to = phone 
      )
  return phone







