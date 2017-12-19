
def is_leap_year(year):
    """
    Nice other solution (http://exercism.io/submissions/9849931d31d54fb19b0a20dcb25dafa9):

    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    """
    is_leap_year = False
    if not year % 4:
        is_leap_year = True
    if not year % 4 and not year % 100:
        is_leap_year = False
    if not year % 4 and not year % 100 and not year % 400:
        is_leap_year = True

    return is_leap_year
