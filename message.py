import os
from twilio.rest import Client
import random

otp = random.randint(1000,9000)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(

                              body='your otp is '+str(otp),
                              from_='#Num', #add a number here
                              to='#Num' #add a number here
                          )
print('Done')
print(message.sid)
