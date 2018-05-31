from datetime import datetime


def time_now():
    now = datetime.now()
    actual_time = (datetime(
        now.year, now.month, now.day,
        now.hour, now.minute))
    time = str(actual_time)[:-12]
    time = time.split("-")
    return time


def last_day_of_month(year, month):
    """ Work out the last day of the month """
    last_days = [31, 30, 29, 28, 27]
    for i in last_days:
        try:
            end = datetime(year, month, i)
        except ValueError:
            continue
        else:
            return end.date()
    return None


def compare_time(last_month_day):
    now = datetime.now()
    actual_time = (datetime(
        now.year, now.month, now.day,
        now.hour, now.minute))
    if str(actual_time)[:-9] == str(last_month_day):
        return False
    else:
        return True
