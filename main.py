from twilio.rest import Client
from dotenv import load_dotenv
import os
import datetime
import time

load_dotenv() # loading our auth tokens from env file 

Sid = os.getenv('SID')  # getting SID
auth_token = os.getenv('Auth_Token')  # getting authToken

def sendMessage(message):
    client = Client(Sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=os.getenv('Sender_Number'),
        to=os.getenv('Reciever_Number')
    )
    print(f"Message sent: {message.sid}")

target_time = datetime.datetime(2023, 2, 16, 20, 30, 0) # yyyy, m, dd, hh, mm, ss

while datetime.datetime.now() < target_time:
    time.sleep(1)

if datetime.datetime.now() >= target_time:
    message = "This message should deliver at 8:30pm on February 16, 2023"
    sendMessage(message)

