from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse


def meetup_day(year, month, day_of_the_week, which):
    occurances = []
    day = date(year, month, 1)
    next_month = day + relativedelta(months=1)
    while True:
        if day.strftime('%A') == day_of_the_week:
            occurances.append(day)
            if which == 'teenth' and day.day in range(13, 20):
                return day

        # break out of loop when next month
        day += relativedelta(days=1)
        if day == next_month:
            break

    if which == 'first':
        return occurances[0]
    if which == 'last':
        return occurances[-1]

    # check 1st, 2nd abbrev etc.
    try:
        return occurances[parse(which).day - 1]
    except IndexError:
        raise ValueError('This day is not in the month!')
