import time
from timings import job1, job2
import schedule


schedule.every().thursday.at("23:20:40").do(job1)
schedule.every().thursday.at("23:21:20").do(job2)


# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
