from twilio.rest import Client
from dotenv import load_dotenv
import os 

load_dotenv()

Sid = os.getenv('SID')
auth_token = os.getenv('Auth_Token')

client = Client(Sid, auth_token)

Text = "Hello World!"

message = client.messages.create(
    body= Text,
    from_=os.getenv('Sender_Number'),
    to=os.getenv('Reciever_Number')
)

print(message.sid)
