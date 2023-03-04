from apscheduler.schedulers.background import BackgroundScheduler
from . views import updateViewCount

thirty_mins = 1800

# WE Want to update user nutrition values after 30 days


# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(updateViewCount, 'interval',
#                       seconds=thirty_mins)
#     scheduler.start()
