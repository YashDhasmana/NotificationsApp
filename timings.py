import datetime
from main import sendMessage


def job1():
    today = datetime.datetime.today()
    if today.weekday() == 4: # 0 for Monday
        message = "First Message at 4:30PM"
        sendMessage(message)


def job2():
    today = datetime.datetime.today()
    if today.weekday() == 4: 
        message = "Second Message at 5:00PM"
        sendMessage(message)

def job3():
    today = datetime.datetime.today()
    if today.weekday() == 4: 
        message = "Third Message at 5:30PM"
        sendMessage(message)

        
def job4():
    today = datetime.datetime.today()
    if today.weekday() == 4: 
        message = "Fourth Message at 6:00PM"
        sendMessage(message)

def job5():
    today = datetime.datetime.today()
    if today.weekday() == 4: 
        message = "Fifth Message at 6:30PM"
        sendMessage(message)                        

