# scheduler.py

import schedule
import time
import os

def send_scheduled_email():
    # Use Django's manage.py to call the custom management command
    os.system('python manage.py send_scheduled_email')

# Schedule the task to run every day at a specific time (adjust as needed)
schedule.every().day.at("10:00").do(send_scheduled_email)

while True:
    schedule.run_pending()
    time.sleep(1)
