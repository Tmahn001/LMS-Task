from time import sleep
from celery import shared_task
import base64
from io import BytesIO

import pandas as pd
from celery import shared_task

from .parser import load_csv



def read_csv_data(csv_file):
    csv_file = base64.b64decode(csv_file)
    bo_data = BytesIO(csv_file)
    data = pd.read_csv(bo_data)
    lead = load_csv(data)
    return lead