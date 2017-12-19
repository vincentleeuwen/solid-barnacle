def is_isogram(string):
    """
    Interesting solution: http://exercism.io/submissions/dfa96d91e24d4176a0cfb9c76da72806
    """
    chars = []
    for s in string.replace(' ', '').replace('-', '').lower():
        if s in chars:
            return False
        else:
            chars.append(s)

    return True
