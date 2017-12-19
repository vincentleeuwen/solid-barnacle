import string


def is_pangram(sentence):
    for char in string.ascii_lowercase:
        if char not in sentence.lower():
            return False
    return True
