def is_isogram(string):
    chars = []
    for s in string.replace(' ', '').replace('-', '').lower():
        if s in chars:
            return False
        else:
            chars.append(s)

    return True
