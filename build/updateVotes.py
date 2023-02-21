from apscheduler.schedulers.background import BackgroundScheduler
from . views import updateViewCount

one_hour = 300

# WE Want to update user nutrition values after 30 days


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(updateViewCount, 'interval',
                      seconds=one_hour)
    scheduler.start()
