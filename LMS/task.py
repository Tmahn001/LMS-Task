import base64
from io import BytesIO
from time import sleep

import pandas as pd
from celery import shared_task
from celery.decorator import task




@shared_task
def test():
    print("it is working")

test.run()

