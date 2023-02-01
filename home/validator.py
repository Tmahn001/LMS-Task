import datetime as d

import phonenumbers
import pytz
from django.conf import settings


def check_time() -> bool:
    zonal_time = pytz.timezone("Asia/Kolkata")
    current_hour = d.datetime.now(zonal_time).hour
    if int(settings.UPLOAD_START_HOUR) <= current_hour <= int(settings.UPLOAD_END_HOUR):
        return True
    return False

