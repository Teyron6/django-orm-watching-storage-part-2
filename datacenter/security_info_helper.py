from datetime import datetime, timezone
from django.utils.timezone import localtime


def is_visit_long(duration, minutes=60):

    seconds = minutes * minutes
    long_visit = duration.total_seconds()>seconds

    return long_visit


def format_duration(duration):
    seconds = duration.total_seconds()
    one_hour_in_seconds = 3600
    one_hour_in_minutes = 60
    one_minute_in_seconds = 60
    hours = int(seconds // one_hour_in_seconds)
    minutes = int((seconds % one_hour_in_seconds) // one_hour_in_minutes)
    seconds = int(seconds % one_minute_in_seconds)
    return '{:2}:{:2}:{:2}'.format(hours, minutes, seconds)


def get_duration(visit):
    entry_local_time = localtime(visit.entered_at)
    if visit.leaved_at == None:
        date_now = localtime(datetime.now(timezone.utc))
        delta = date_now - entry_local_time
    else:
        leaved_local_time = localtime(visit.leaved_at)
        delta = leaved_local_time - entry_local_time
    return delta