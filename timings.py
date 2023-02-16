import datetime
from main import sendMessage


def job1():
    today = datetime.datetime.today()
    if today.weekday() == 3: # 0 for Monday
        message = "Namaste World! 01"
        sendMessage(message)


def job2():
    today = datetime.datetime.today()
    if today.weekday() == 3: 
        message = "Namaste World! 02"
        sendMessage(message)

