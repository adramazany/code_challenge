"""scheduler.py:
    Provide Internal Scheduler to execute etl process in 10 minute intervals
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from eurowings import config
from eurowings.searches import Searches
from eurowings.visitors import Visitors


class Scheduler:
    scheduler = BlockingScheduler()

    def start(self):
        if config.etl_scheduler_interval_minutes>0:
            self.scheduler.add_job(self.etl_job, 'interval', minutes=config.etl_scheduler_interval_minutes)
            self.scheduler.start()

    def etl_job(self):
        count,max_modified_date = Visitors().etl()
        print('visitors etl done : ',{'count':count,'max_modified_date':max_modified_date},datetime.datetime.now())
        count,max_modified_date = Searches().etl()
        print('visitors etl done : ',{'count':count,'max_modified_date':max_modified_date},datetime.datetime.now())

