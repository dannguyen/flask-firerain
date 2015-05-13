from datetime import datetime
from math import radians, cos, sin, asin, sqrt
import pytz
SYS_TIMEZONE_STR = 'US/Pacific'

def get_system_tz():
    """
    returns: <DstTzInfo 'US/Pacific' LMT-1 day, 16:07:00 STD>
    """
    return pytz.timezone(SYS_TIMEZONE_STR)

def get_current_datetime():
    return datetime.now(tz = get_system_tz())


def get_system_datetime_str(epoch_sec):
    dt = datetime.fromtimestamp(epoch_sec, tz = get_system_tz())
    return dt

def get_time_since(epoch_sec, dy = None):
    dy = get_current_datetime() if not dy else dy
    dt = datetime.fromtimestamp(epoch_sec, tz = get_system_tz())
    delta = dy - dt
    if delta.days > 2:
        return "%d days ago" % delta.days
    else:
        return "%s hours ago" % round((delta.total_seconds() / 3600), 1)


RADIUS_OF_EARTH_IN_MILES = 3956
def haversine(lng1, lat1, lng2, lat2):
    """
    returns distance in miles
    """
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    # haversine formula
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat /2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = RADIUS_OF_EARTH_IN_MILES
    return c * r
