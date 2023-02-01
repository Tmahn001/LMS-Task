import base64
from io import BytesIO
from time import sleep

import pandas as pd
from celery import shared_task
from celery.decorator import task




@task
def test(duration):
    sleep(duration)
    print("it is working")

test.delay()