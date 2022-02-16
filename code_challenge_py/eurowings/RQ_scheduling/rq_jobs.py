from rq import Queue
from redis import Redis
import requests


def count_words_at_url(url):
    resp = requests.get(url)
    print(url, len(resp.text.split()))


def add_job_to_queue(taskQueue,url):
    taskQueue.enqueue( count_words_at_url,url)
    print(url," added to queue.")
