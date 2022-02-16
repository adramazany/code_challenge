from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print( "Decorated job")

scheduler = BlockingScheduler()
# scheduler.add_job(some_job, 'interval', hours=1)
scheduler.add_job(some_job, 'interval', minutes=1)
# scheduler.add_job(some_job, 'interval', seconds=1)
scheduler.start()