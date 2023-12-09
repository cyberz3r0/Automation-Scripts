from login import timesheet
from discord import discord

import schedule
from time import sleep

schedule.every().tuesday.at("11:00", "America/Los_Angeles").do(timesheet)
schedule.every().tuesday.at("10:59", "America/Los_Angeles").do(discord)
schedule.every().wednesday.at("11:00", "America/Los_Angeles").do(timesheet)
schedule.every().wednesday.at("10:59", "America/Los_Angeles").do(discord)
schedule.every().thursday.at("11:00", "America/Los_Angeles").do(timesheet)
schedule.every().thursday.at("10:59", "America/Los_Angeles").do(discord)
schedule.every().friday.at("11:00", "America/Los_Angeles").do(timesheet)
schedule.every().friday.at("10:59", "America/Los_Angeles").do(discord)
schedule.every().saturday.at("11:00", "America/Los_Angeles").do(timesheet)
schedule.every().saturday.at("10:59", "America/Los_Angeles").do(discord)

schedule.every().tuesday.at("15:00", "America/Los_Angeles").do(timesheet)
schedule.every().tuesday.at("15:01", "America/Los_Angeles").do(discord)
schedule.every().wednesday.at("15:00", "America/Los_Angeles").do(timesheet)
schedule.every().wednesday.at("15:01", "America/Los_Angeles").do(discord)
schedule.every().thursday.at("15:00", "America/Los_Angeles").do(timesheet)
schedule.every().thursday.at("15:01", "America/Los_Angeles").do(discord)
schedule.every().friday.at("15:00", "America/Los_Angeles").do(timesheet)
schedule.every().friday.at("15:01", "America/Los_Angeles").do(discord)
schedule.every().saturday.at("15:00", "America/Los_Angeles").do(timesheet)
schedule.every().saturday.at("15:01", "America/Los_Angeles").do(discord)

schedule.every().tuesday.at("16:00", "America/Los_Angeles").do(timesheet)
schedule.every().tuesday.at("16:01", "America/Los_Angeles").do(discord)
schedule.every().wednesday.at("16:00", "America/Los_Angeles").do(timesheet)
schedule.every().wednesday.at("16:01", "America/Los_Angeles").do(discord)
schedule.every().thursday.at("16:00", "America/Los_Angeles").do(timesheet)
schedule.every().thursday.at("16:01", "America/Los_Angeles").do(discord)
schedule.every().friday.at("16:00", "America/Los_Angeles").do(timesheet)
schedule.every().friday.at("16:01", "America/Los_Angeles").do(discord)
schedule.every().saturday.at("16:00", "America/Los_Angeles").do(timesheet)
schedule.every().saturday.at("16:01", "America/Los_Angeles").do(discord)

schedule.every().tuesday.at("20:00", "America/Los_Angeles").do(timesheet)
schedule.every().tuesday.at("19:59", "America/Los_Angeles").do(discord)
schedule.every().wednesday.at("20:00", "America/Los_Angeles").do(timesheet)
schedule.every().wednesday.at("19:59", "America/Los_Angeles").do(discord)
schedule.every().thursday.at("20:00", "America/Los_Angeles").do(timesheet)
schedule.every().thursday.at("19:59", "America/Los_Angeles").do(discord)
schedule.every().friday.at("20:00", "America/Los_Angeles").do(timesheet)
schedule.every().friday.at("19:59", "America/Los_Angeles").do(discord)
schedule.every().saturday.at("20:00", "America/Los_Angeles").do(timesheet)
schedule.every().saturday.at("19:59", "America/Los_Angeles").do(discord)


jobs = schedule.get_jobs()
new_jobs=(str(jobs)).split("),")
for job in new_jobs:
    print(job)
from helper import show_notification
show_notification("Task","Started")
while True:
    schedule.run_pending()
    sleep(1)
