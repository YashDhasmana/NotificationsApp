import time
from timings import *
import schedule


schedule.every().friday.at("16:30:00").do(job1)
schedule.every().friday.at("17:00:00").do(job2)
schedule.every().friday.at("17:30:00").do(job3)
schedule.every().friday.at("18:00:00").do(job4)
schedule.every().friday.at("18:30:00").do(job5)


# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
