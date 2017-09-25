from celery import shared_task
import time


@shared_task
def celery_test(sleep=1):
    print('I will sleep {}s'.format(sleep))
    time.sleep(sleep)
    print('I wake up')
    return 'abc'
