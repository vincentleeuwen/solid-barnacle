from datetime import timedelta


def add_gigasecond(birth_date):
    try:
        return birth_date + timedelta(seconds=10**9)
    except TypeError:
        raise ValueError('Input must be a datetime object')
