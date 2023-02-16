from twilio.rest import Client
from dotenv import load_dotenv
import os

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

