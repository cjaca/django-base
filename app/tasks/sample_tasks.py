import time
import requests
import random

from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command

logger = get_task_logger(__name__)

class BaseTaskWithRetry(celery.Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {'max_retries': 5}
    retry_backoff=5
    retry_jitter=True

@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@shared_task
def sample_task():
    logger.info("The sample task just ran.")


@shared_task
def send_email_report():
    call_command("email_report", )


@shared_task(bind=True, base=BaseTaskWithRetry)
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('https://httpbin.org/delay/5')
