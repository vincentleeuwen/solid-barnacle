
def verify(isbn):
    clean_isbn = list(''.join(isbn.split('-')))
    if len(clean_isbn) != 10:
        return False
    if clean_isbn[-1] == 'X':
        clean_isbn[-1] = 10
    try:
        return sum([int(obj) * (10 - index) for index, obj in enumerate(clean_isbn)]) % 11 == 0
    except ValueError:
        return False
