from login import timesheet
import schedule
from time import sleep

schedule.every().tuesday.at("11:00").do(timesheet)
schedule.every().wednesday.at("11:00").do(timesheet)
schedule.every().thursday.at("11:00").do(timesheet)
schedule.every().friday.at("11:00").do(timesheet)
schedule.every().saturday.at("11:00").do(timesheet)

schedule.every().tuesday.at("15:00").do(timesheet)
schedule.every().wednesday.at("15:00").do(timesheet)
schedule.every().thursday.at("15:00").do(timesheet)
schedule.every().friday.at("15:00").do(timesheet)
schedule.every().saturday.at("15:00").do(timesheet)

schedule.every().tuesday.at("16:00").do(timesheet)
schedule.every().wednesday.at("16:00").do(timesheet)
schedule.every().thursday.at("16:00").do(timesheet)
schedule.every().friday.at("16:00").do(timesheet)
schedule.every().saturday.at("16:00").do(timesheet)

schedule.every().tuesday.at("20:00").do(timesheet)
schedule.every().wednesday.at("20:00").do(timesheet)
schedule.every().thursday.at("20:00").do(timesheet)
schedule.every().friday.at("20:00").do(timesheet)
schedule.every().saturday.at("20:00").do(timesheet)

jobs = schedule.get_jobs()
new_jobs=(str(jobs)).split("),")
for job in new_jobs:
    print(job)
while True:
    schedule.run_pending()
    sleep(1)
