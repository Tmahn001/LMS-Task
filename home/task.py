import base64
from io import BytesIO

import pandas as pd
from LMS.celery import shared_task

from .parser import load_csv


@shared_task
def open_csv_data(csv_file):
    csv_file = base64.b64decode(csv_file)
    bo_data = BytesIO(csv_file)
    data = pd.read_csv(bo_data)
    lead = load_csv(data)
    return lead