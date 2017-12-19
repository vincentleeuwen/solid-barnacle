import string


def is_pangram(sentence):
    try:
        sentence.lower()
    except AttributeError:
        raise Exception('Thats not a proper sentence!')
    else:
        for char in string.ascii_lowercase:
            if char not in sentence.lower():
                return False
        return True
