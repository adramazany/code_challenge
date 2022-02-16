# import threading
from rq import Queue
# from redis import Redis
import requests
from redislite import Redis

from eurowings.RQ_scheduling import rq_jobs

r = Redis()
print(r)
taskQueue = Queue('task',connection=r)

counter=1
for i in range(3):
    url='http://nvie.com?%s'%i
    # t = threading.Thread(target=add_job_to_queue, args=(taskQueue,url,))
    # t.start()
    rq_jobs.add_job_to_queue(taskQueue,url)

