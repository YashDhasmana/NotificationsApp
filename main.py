from twilio.rest import Client
from dotenv import load_dotenv
import os
import datetime
import time
import schedule


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


def job():
    today = datetime.datetime.today()
    if today.weekday() == 3: # 0 for Monday
        message = "Hello World!"
        sendMessage(message)


# Schedule the job to run every Thursday at 9:30 PM
schedule.every().thursday.at("21:30:30").do(job)


# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
